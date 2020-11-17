import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10


#pagination
def paginate_questions(request, questions):
    page = request.args.get('page', 1, type=int)
    start = (page-1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    formatted_questions = [question.format() for question in questions]
    current_page_questions = formatted_questions[start:end]
    return current_page_questions


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

    #CORS Setup for Origins
    CORS(app, resources={r"/api/*":{"origins": "*"}})

    # after_request decorator to set Access Control Allow
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers','Content-Type, Authorization, true')
        response.headers.add('Access-Control-Allow-Methods','GET,PUT,POST,DELETE,OPTIONS')
        return response

    #GET request for all categories
    @app.route('/categories', methods=['GET'])
    def get_categories():
        categories = Category.query.all()
        formatted_categories = {category.id: category.type for category in categories}
        return jsonify({
            'success': True,
            'categories': formatted_categories,
        })

    #GET request for all questions
    @app.route('/questions', methods=['GET'])
    def get_questions():
        questions = Question.query.all()
        current_page_questions = paginate_questions(request, questions)
        categories = list(map(Category.format, Category.query.all()))
        if len(current_page_questions) == 0:
           abort(404) 
        return jsonify({
            "success": True,
            "questions": current_page_questions,
            "total_questions": len(Question.query.all()),
            "categories": categories,
            "current_category": None
        })

    #Endpoint to POST a new # question
    @app.route('/questions', methods=['POST'])
    def add_question():
        body = request.get_json()
        question = body.get('question', None)
        answer = body.get('answer', None)
        category = body.get('category', None)
        difficulty = body.get('difficulty', None)
        valid_flag = [question, answer, category, difficulty]
        if all(valid_flag) is False:
            abort(400)
        try:
            question = Question(question=question, answer=answer, category=category, difficulty=difficulty)
            question.insert()
            questions = Question.query.order_by(Question.id).all()
            current_page_questions = paginate_questions(request, questions)
            return jsonify({
                "success": True,
                "created": question.id,
                "questions": current_page_questions,
                "total_questions": len(Question.query.all())
            })
        except Exception:
            abort(500)
           
#End Point to delete a question using question # ID
    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    def delete_question(question_id):
        question = Question.query.filter(Question.id == question_id).one_or_none()
        if question is None:
            abort(404)

        question.delete()
        selection = Question.query.order_by(Question.id).all()
        current_questions = [question.format() for question in selection]

        return jsonify({
            "success": True,
            "deleted": question_id,
            "questions": current_questions,
            "total_questions": len(Question.query.all())
        })

    #POST endpoint to get questions based on search term
    @app.route('/search', methods=['POST'])
    def search_questions():
        try:
            body = request.get_json()
            search = body.get('searchTerm', None)
            if search is not None:
                questions = Question.query.order_by(Question.id).filter(
                    Question.question.ilike('%{}%'.format(search)))
                questions = [question.format() for question in questions.all()]
                return jsonify({
                    "success": True,
                    "questions": questions,
                    "total_matched_questions": len(questions)
                })
            else:
                abort(422)
        except Exception:
            abort(404)

    #GET questions based on category
    @app.route('/categories/<int:category_id>/questions', methods=['GET'])
    def get_questions_by_category(category_id):
        try:
            available_category = Category.query.filter(Category.id == category_id).one_or_none()
            questions = Question.query.filter(Question.category == category_id).order_by(Question.id).all()
            questions = [question.format() for question in questions]
            if available_category is None:
                abort(404) 
            else:
                return jsonify({
                    "success": True,
                    "questions": questions,
                    "total_questions": len(questions),
                    "current_category": category_id
                })
        except Exception:
            abort(404)

    #POST endpoint to get questions to play the quiz
    @app.route('/play', methods=['POST'])
    def get_quiz_questions():
        body = request.get_json()
        previous_questions = body.get('previous_questions', [])
        quiz_category = body.get('quiz_category', None)
        selection = []

        try:
            if quiz_category is not None:
                if quiz_category['id'] == 0:
                    selection = Question.query.all()
                else:
                    selection = Question.query.filter(Question.category == quiz_category['id']).all()
                
                question_set = [question.format() for question in selection if question.id not in previous_questions] 
                
                if len(question_set) == 0:
                    return jsonify({
                        "success": True,
                        "question": None
                    })
                question = random.choice(question_set)
                return jsonify({
                    "success": True,
                    "question": question
                })
        except Exception:
            abort(422)

    #Error Handlers
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Resource Not Found"
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "Unprocessable"
        }), 422

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Bad Request"
        }), 400 

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "Internal Server Error"
        }), 500

    return app
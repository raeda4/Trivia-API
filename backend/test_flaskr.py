import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category
from config import database_setup
from sqlalchemy import desc


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client        
        self.database_username = "postgres"
        self.database_password = "postgres"
        self.database_name = "trivia_test"
        self.database_path = "postgres://{}:{}@{}/{}".format(self.database_username, self.database_password, 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    #Getting Categories Test
    def test_get_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['categories'])

    #Get Categories - failure
    def test_get_categories_404(self):
        res = self.client().get('category')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False) 
        self.assertEqual(data['message'], 'Resource Not Found')
        
    #Getting Paginated Questions
    def test_get_paginated_questions(self):
        res = self.client().get('/questions')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['categories']))
        self.assertTrue(len(data['questions']))

    #404 Paginated Qeustions Unavailable
    def test_404_paginated_questions(self):
        res = self.client().get('/questions?page=10000')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource Not Found')

    #Get questions by Categories - Success
    def test_get_questions_by_category(self):
        res = self.client().get('/categories/1/questions?page=1')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_questions'])
        self.assertTrue(data['current_category'])
        self.assertTrue(len(data['questions']))

    #Get questions by Categories - failure
    def test_get_questions_by_category(self):
        res = self.client().get('/categories/1400/questions?page=1')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource Not Found')
    
    #Adding a new question
    def test_add_new_question(self): #changed 'post' to 'add' because this was running after the delete test and causing it to fail
        post_data = {
        'question': 'new question',
        'answer': 'new answer',
        'difficulty': 1,
        'category': 1
        }
        res = self.client().post('/questions', json=post_data)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    #Adding a new question - missing input 400
    def test_post_new_question_400(self):
        post_data = {
        'question': 'new question',
        'answer': 'new answer',
        'difficulty': 1,
        }
        res = self.client().post('/questions', json=post_data)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Bad Request")

    #Deleting a question using question id
    def test_delete_question(self):

        new_question = Question.query.filter(Question.question.ilike('new question')).first()
        new_question_id = str(new_question.id)
        res = self.client().delete('/questions/' + new_question_id)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    #Deleting a question failure with 404
    def test_delete_question_404(self):
        res = self.client().delete('/questions/10000000') 
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Resource Not Found")

    #Search
    def test_search_question(self):
        post_data = {
            'searchTerm': 'name' #Switched to name to work with the base test data
        }
        res = self.client().post('/search', json=post_data)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["total_matched_questions"])
        self.assertTrue(len(data["questions"]))

    #Search 404
    def test_search_question_404(self):
        res = self.client().post('/search')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Resource Not Found")

    #Play quiz failure with 422
    def test_play_quiz_422(self):
        post_data = {
            'previous_question': [],
            'quiz_category': {
                'type': 'Science'
            }
        }
        res = self.client().post('/play', json=post_data)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Unprocessable")

    #Play quiz
    def test_play_quiz(self):
        post_data = {
            'previous_questions': [],
            'quiz_category': {
                'type': 'Science',
                'id': 1
            }
        }
        res = self.client().post('/play', json=post_data)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
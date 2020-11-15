# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```
    ---> use instead psql postgres postgres < trivia.psql
    ---> psql trivia_test postgress < trivia.psql

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## Tasks

One note before you delve into your tasks: for each endpoint you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior. 

X 1. Use Flask-CORS to enable cross-domain requests and set response headers. 
X 2. Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories. 
X 3. Create an endpoint to handle GET requests for all available categories. 
X 4. Create an endpoint to DELETE question using a question ID. 
X 5. Create an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score. 
X 6. Create a POST endpoint to get questions based on category. 
X 7. Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question. 
X 8. Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions. 
X 9. Create error handlers for all expected errors including 400, 404, 422 and 500. 

REVIEW_COMMENT
```
This README is missing documentation of your endpoints. Below is an example for your endpoint to get all categories. Please use it as a reference for creating your documentation and resubmit your code. 

Endpoints
1. GET '/categories'
2. GET '/questions?page=<page_number>'
3. POST '/questions'
4. DELETE '/questions/<int:question_id>'
5. POST '/search'
6. GET '/categories/<int:category_id>/questions'
7. POST '/play'

Details of Endpoints

1. GET '/categories'
    - Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
    - Request Arguments: None
    - Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs. 
        {'1' : "Science",
        '2' : "Art",
        '3' : "Geography",
        '4' : "History",
        '5' : "Entertainment",
        '6' : "Sports"}

2. GET '/questions?page=<page_number>'
    -Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
    -Fetches a dictionary of paginated questions. 10 questions per page. The keys are question, answer, category, difficulty, and ID
    -Requested Arguments: page number
    -Returns: a list of categories, the current category, total questions, and a list of questions for the current page
        Example: 
        {
            "categories": [
                {
                  "id": 1, 
                  "type": "Science"
                }, 
                {
                  "id": 2, 
                  "type": "Art"
                }, 
                {
                  "id": 3, 
                  "type": "Geography"
                }, 
                {
                  "id": 4, 
                  "type": "History"
                }, 
                {
                  "id": 5, 
                  "type": "Entertainment"
                }, 
                {
                  "id": 6, 
                  "type": "Sports"
                }
            ],             
            "current_category": null, 
            "questions": [
                {
                  "answer": "Maya Angelou", 
                  "category": 4, 
                  "difficulty": 2, 
                  "id": 5, 
                  "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
                }, 
                {
                  "answer": "Muhammad Ali", 
                  "category": 4, 
                  "difficulty": 1, 
                  "id": 9, 
                  "question": "What boxer's original name is Cassius Clay?"
                }, 
                {
                  "answer": "Apollo 13", 
                  "category": 5, 
                  "difficulty": 4, 
                  "id": 2, 
                  "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
                }, 
                {
                  "answer": "Tom Cruise", 
                  "category": 5, 
                  "difficulty": 4, 
                  "id": 4, 
                  "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
                }, 
                {
                  "answer": "Edward Scissorhands", 
                  "category": 5, 
                  "difficulty": 3, 
                  "id": 6, 
                  "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
                }, 
                {
                  "answer": "Brazil", 
                  "category": 6, 
                  "difficulty": 3, 
                  "id": 10, 
                  "question": "Which is the only team to play in every soccer World Cup tournament?"
                }, 
                {
                  "answer": "Uruguay", 
                  "category": 6, 
                  "difficulty": 4, 
                  "id": 11, 
                  "question": "Which country won the first ever soccer World Cup in 1930?"
                }, 
                {
                  "answer": "George Washington Carver", 
                  "category": 4, 
                  "difficulty": 2, 
                  "id": 12, 
                  "question": "Who invented Peanut Butter?"
                }, 
                {
                  "answer": "Lake Victoria", 
                  "category": 3, 
                  "difficulty": 2, 
                  "id": 13, 
                  "question": "What is the largest lake in Africa?"
                }, 
                {
                  "answer": "The Palace of Versailles", 
                  "category": 3, 
                  "difficulty": 3, 
                  "id": 14, 
                  "question": "In which royal palace would you find the Hall of Mirrors?"
                }
            ],   
            "success": true, 
            "total_questions": 24
        }


3. POST '/questions'
    -Creates a new question
    -Request Arguments: question, answer, category, difficulty
        Example: {
            'question': 'new question',
            'answer': 'new answer',
            'difficulty': 1,
            }
    -Returns: successful payload
        Example: {
            "success": True,
            "created": 45,
            "questions": [
                {
                    "answer": "Maya Angelou", 
                    "category": 4, 
                    "difficulty": 2, 
                    "id": 5, 
                    "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
                }
            ]
            "total_questions": 45
        }

4. DELETE '/questions/<int:question_id>'
    -Deletes desired question based on question id
    -Request Arguments: Question ID
    -Returns: sucessful payload if question has been deleted
        Example:
        {
        "success": True,
            "deleted": 50,
            "questions": [
                {
                    "answer": "Maya Angelou", 
                    "category": 4, 
                    "difficulty": 2, 
                    "id": 5, 
                    "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
                }
            ]
            "total_questions": 50
        }

5. POST '/search'
    -Searches questions base on provided argument
    -Request Arguments: search term
        Example: {"searchTerm": "World Cup"}
    -Returns: list of questions containing the search term
        Example: 
            {
                "questions": [
                  {
                    "answer": "Brazil",
                    "category": 6,
                    "difficulty": 3,
                    "id": 10,
                    "question": "Which is the only team to play in every soccer World Cup tournament?"
                  },
                  {
                    "answer": "Uruguay",
                    "category": 6,
                    "difficulty": 4,
                    "id": 11,
                    "question": "Which country won the first ever soccer World Cup in 1930?"
                  }
                ],
                "success": true,
                "total_matched_questions": 2
            }

6. GET '/categories/<int:category_id>/questions'
    -Fetch questions based on desired category
    -Request Arguments: Category ID and Page Number
    -Returns: a list of questions from the desired category
        Example:
        {
            "current_category": 2,
            "questions": [
              {
                "answer": "Escher",
                "category": 2,
                "difficulty": 1,
                "id": 16,
                "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
              },
              {
                "answer": "Mona Lisa",
                "category": 2,
                "difficulty": 3,
                "id": 17,
                "question": "La Giaconda is better known as what?"
              },
              {
                "answer": "One",
                "category": 2,
                "difficulty": 4,
                "id": 18,
                "question": "How many paintings did Van Gogh sell in his lifetime?"
              },
              {
                "answer": "Jackson Pollock",
                "category": 2,
                "difficulty": 2,
                "id": 19,
                "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
              }
            ],
            "success": true,
            "total_questions": 4
        }


7. POST '/play'
    -Post your previous questions and desired category to get a new question to answer during a quiz
    -Request Arguments: Previous Qeustions and Selected Category
        Example:
        '{"previous_questions": [5, 2], "quiz_category": {"id": 4, "type": "History"} }'
    -Returns: A question that is not in the list of previous questions and within the desired category
        Example:
        {
            "question": {
              "answer": "George Washington Carver",
              "category": 4,
              "difficulty": 2,
              "id": 12,
              "question": "Who invented Peanut Butter?"
            },
            "success": true
        }




```


## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```
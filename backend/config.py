import os
SECRET_KEY = os.urandom(32)

# reference back to the script
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_TRACK_MODIFICATIONS = False

database_setup = {
    "database_name_production": "trivia",
    "database_name_test": "trivia_test",
    "user_name": "student",
    "password": "1234",
    "port": "localhost:5432"
}
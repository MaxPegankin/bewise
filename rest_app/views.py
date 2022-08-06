from rest_app import app
from rest_app.database import db_session
from rest_app.models import Quiz

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/add_question')
def add_question():
    new_question = Quiz("What?", "That!")
    db_session.add(new_question)
    db_session.commit()

    return f'Question:{new_question.question} with answer:{new_question.answer} and ID:{new_question.id} was added to DB' 

    
from datetime import date
from rest_app import app
from flask import Flask, render_template
from rest_app.database import db_session
from rest_app.models import Quiz
from rest_app.forms import QuestionsRequestForm

from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField

import requests, json
from datetime import datetime

@app.route('/', methods=['GET', 'POST'])
def index():
    added_questions = []
    form = QuestionsRequestForm()
    if form.validate_on_submit():
        questions_num = form.questions_num.data
        # print(questions_num)
        for i in range(1, questions_num+1):
            #request data
            url = 'https://jservice.io/api/random?count=1'
            added_question = None
            while not added_question:
                r = requests.get(url)
                data = json.loads(r.text.strip('[]'))
                #print(data.get('id'))
                #try to add to db
                creation_date = datetime.strptime(data.get('created_at')[:10], '%Y-%m-%d')
                added_question = add_question_to_db(data.get('id'), data.get('question'), data.get('answer'), creation_date)
            added_questions.append(added_question)

    form.questions_num.process("1")
    return render_template('index.html', form=form, added_questions=added_questions)

def add_question_to_db(question_id:int, question: str, answer: str, creation_date:date) -> str:
    if Quiz.query.filter(Quiz.question_id == 1).first(): return None
    new_question = Quiz(question_id, question, answer, creation_date)
    db_session.add(new_question)
    db_session.commit()
    #print(f'Question:{new_question.question} with answer:{new_question.answer} and ID:{new_question.question_id} was added to DB' )
    return new_question.question 

    
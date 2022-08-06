from datetime import datetime
from sqlalchemy import Column, Integer, Text, Date
from datetime import date
from rest_app.database import Base
#1. ID вопроса, 2. Текст вопроса, 3. Текст ответа, 4. - Дата создания вопроса
class Quiz(Base):
    __tablename__ = 'quiz'
    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, unique=True)
    question = Column(Text)
    answer = Column(Text)
    creation_date = Column(Date)

    def __init__(self, question_id:int=None, question:str=None, answer:str=None, creation_date:date=date.today()):
        self.question_id = question_id
        self.question = question
        self.answer = answer
        self.creation_date = creation_date

    def __repr__(self):
        return f'<Quiz {self.question!r}>'
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class QuestionsRequestForm(FlaskForm):
    questions_num = IntegerField('How many questions do you want?', validators=[DataRequired(), NumberRange(min=1, max=100, message='Not so many please')], default=1)
    submit = SubmitField('Submit')
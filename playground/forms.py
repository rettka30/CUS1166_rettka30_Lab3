from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from wtforms import TextAreaField
from wtforms.validators import Length


class CourseForm(FlaskForm):
    course_title = StringField('Course Title', validators=[DataRequired()])
    course_number = StringField('Course Number', validators=[DataRequired()])
    submit = SubmitField('Submit')

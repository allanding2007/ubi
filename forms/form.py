"""
    File Name: form.py
    Created On: 2017/03/30/
    Description: This file is about some forms, according to
    the models.
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    """
    Description: This form is used for login.
    """
    name = StringField("Your Name?", validators=[DataRequired()])
    password = PasswordField("Your Password?", validators=[DataRequired()])
    submit = SubmitField("Submit")

"""
    File Name: form.py
    Created On: 2017/03/30/
    Description: This file is about some forms, according to
    the models.
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms import DateTimeField, BooleanField, TextAreaField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    """
    Description: This form is used for login.
    """
    name = StringField("Your Name?", validators=[DataRequired()])
    password = PasswordField("Your Password?", validators=[DataRequired()])
    submit = SubmitField("Submit")


class DeviceForm(FlaskForm):
    """
    Description: This form is used for device_detail.
    """
    mac_address = StringField("Mac Address:", validators=[DataRequired()])
    manufacturer = StringField("Manufacturer:")
    join_date = DateTimeField("Join Date:")
    is_activated = BooleanField("Is Activated")
    description = TextAreaField("Description:")
    submit = SubmitField("Save")


class SsidForm(FlaskForm):
    """
    Description: This form is used for ssid_config_detail.
    """
    name = StringField("Ssid Name", validators=[DataRequired()])
    pass_word = StringField("Pass Word", validators=[DataRequired()])
    is_activated = BooleanField("Is Activated")
    submit = SubmitField("Save")


class ProfileForm(FlaskForm):
    """
    Description: This form is userd for user profile.
    """
    user_name = StringField("User Name:", validators=[DataRequired()])
    email = StringField("E-mail:", validators=[DataRequired()])
    join_date = DateTimeField("Join Date:")


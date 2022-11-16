from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SearchField, TextAreaField
# Not sure if I'll get to it tonight but SearchField and TextArea field would probably be useful 
# for searching for albums and writing reviews. There was also RadioField which could be used for 
# ratings maybe? Just have radio buttons as options 0-10 or whatever. 
from wtforms.validators import DataRequired, Email

class UserSignupForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    display_name = StringField('Display Name', validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name')
    password = PasswordField('Password', validators=[DataRequired()])
    submit_button = SubmitField()

class UserSigninForm(FlaskForm):
    login = StringField('Email or Display Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit_button = SubmitField()
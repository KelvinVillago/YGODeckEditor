from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField, TextAreaField
from wtforms.validators import InputRequired, EqualTo

class SignUpForm(FlaskForm):
    first_name = StringField('First Name', validators=[InputRequired()])
    last_name = StringField('Last Name', validators=[InputRequired()])
    username = StringField('Username', validators=[InputRequired()])
    email = EmailField('Email', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    confirm_pass = PasswordField('Confirm Password', validators=[InputRequired(),EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Log In')
    
class AddContact(FlaskForm):
    first_name = StringField('First Name', validators=[InputRequired()])
    last_name = StringField('Last Name', validators=[InputRequired()])
    phoneNum = StringField('Phone Number', validators=[InputRequired()])
    address = StringField('Address', validators=[InputRequired()])
    submit = SubmitField('Add Contact')


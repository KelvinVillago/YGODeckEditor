from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import InputRequired, EqualTo

class AddContact(FlaskForm):
    first_name = StringField('First Name', validators=[InputRequired()])
    last_name = StringField('Last Name', validators=[InputRequired()])
    phoneNum = StringField('Phone Number', validators=[InputRequired()])
    address = StringField('Address', validators=[InputRequired()])
    submit = SubmitField('Add Contact')


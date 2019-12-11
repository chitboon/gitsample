from wtforms import StringField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField, Form, PasswordField
from wtforms import validators, ValidationError

class LoginForm(Form):
    id = StringField('UserName', [validators.DataRequired('Please enter your user id.')])
    password = PasswordField('Password', [validators.DataRequired('Please enter your password.')])
    submit = SubmitField('Login')

class RegisterForm(Form):
    id = StringField('UserName', [validators.DataRequired('Please enter your user id.')])
    password = PasswordField('Password', [validators.DataRequired('Please enter your password.')])
    name = StringField('Name', [validators.DataRequired('Please enter your full name.'), validators.Length(min=2, max=15)])
    email = StringField('Email', [validators.InputRequired('Please enter your email.'), validators.Email()])
    submit = SubmitField('Register')

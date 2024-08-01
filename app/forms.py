from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
import re

class StrongPassword:
    def __init__(self, message=None):
        if not message:
            message = 'Password must be at least 8 characters long, contain at least one uppercase letter, one lowercase letter, one digit, and one special character.'
        self.message = message

    def __call__(self, form, field):
        password = field.data
        if len(password) < 8:
            raise ValidationError(self.message)
        if not re.search(r'[A-Z]', password):
            raise ValidationError(self.message)
        if not re.search(r'[a-z]', password):
            raise ValidationError(self.message)
        if not re.search(r'[0-9]', password):
            raise ValidationError(self.message)
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise ValidationError(self.message)


class RegisterForm(FlaskForm):
    username=StringField('Username', validators=[DataRequired(),Length(min=4 , max=20)])
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired(),StrongPassword()])
    conform_password=PasswordField('Conform Password',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('Sign up')


class LoginForm(FlaskForm):
    email=StringField('Email',validator=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    remember=BooleanField('Remember Me')
    submit=SubmitField('Login')
    
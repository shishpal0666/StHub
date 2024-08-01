from flask_wtf import FlaskForm
from flask import flash
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.db import get_db_connection
import re
import email_validator

class StrongPassword:
    def __init__(self, message=None):
        if not message:
            message = 'Password must be at least 8 characters long, contain at least one uppercase letter, one lowercase letter, one digit, and one special character.'
        self.message = message

    def __call__(self, form, field):
        password = field.data
        strong_pass=True
        if len(password) < 8:
            strong_pass=True
        if not re.search(r'[A-Z]', password):
            strong_pass=True
        if not re.search(r'[a-z]', password):
            strong_pass=True
        if not re.search(r'[0-9]', password):
            strong_pass=True
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            strong_pass=True
        if strong_pass:
            flash(self.message,category='danger')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), StrongPassword()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign up')

    def validate_username(self, username):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT username FROM users WHERE username = %s", (username.data,))
        user = cur.fetchone()
        cur.close()
        conn.close()

        if user:
            flash(f"Username already exists! Use a different username.",category='danger')
    
    def validate_email(self, email):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT email FROM users WHERE email = %s", (email.data,))
        email = cur.fetchone()
        cur.close()
        conn.close()

        if email:
            flash(f"Email already exists! Use a different email.",category='danger')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

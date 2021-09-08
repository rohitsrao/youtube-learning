from flaskblog.models import User
from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

class RegistrationForm(FlaskForm):
    username = StringField(
        'Username',
        validators = [
            DataRequired(),
            Length(min=2, max=20),
        ]
    )
    
    email = StringField(
        'Email',
        validators = [
            DataRequired(),
            Email(),
        ]
    )
    
    password = PasswordField(
        'Password',
        validators = [
            DataRequired()
        ]
    )
    
    confirm_password = PasswordField(
        'Confirm password',
        validators=[
            DataRequired(),
            EqualTo('password')
        ]
    )
    
    submit = SubmitField(
        'Sign Up'
    )
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is already taken. Please choose another one')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email address is already taken. Please choose another one')

class LoginForm(FlaskForm):
    email = StringField(
        'Email',
        validators=[DataRequired(), Email()]
    )
    password = PasswordField(
        'Password', 
        validators=[DataRequired()]
    )
    remember = BooleanField(
        'Remember Me'
    )
    submit = SubmitField('Login')


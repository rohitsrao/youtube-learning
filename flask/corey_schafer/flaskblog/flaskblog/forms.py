from flaskblog.models import User
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import BooleanField, PasswordField, StringField, SubmitField, TextAreaField
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

class UpdateAccountForm(FlaskForm):
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

    picture = FileField(
        'Update Profile Picture',
        validators = [
            FileAllowed(['jpg', 'jpeg', 'png'])
        ]
    )

    submit = SubmitField(
        'Update'
    )

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username = username.data).first()
            if user:
                raise ValidationError('That username is already taken. Please choose another one')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email = email.data).first()
            if user:
                raise ValidationError('That email address is already taken. Please choose another one')

class PostForm(FlaskForm):
    title = StringField(
        'Title',
        validators = [
            DataRequired(),
        ]
    )
    
    content = TextAreaField(
        'Content',
        validators = [
            DataRequired(),
        ]
    )

    submit = SubmitField('Post')

class RequestPasswordResetForm(FlaskForm):

    email = StringField(
        'Email',
        validators = [
            DataRequired(),
            Email()
        ]
    )
        
    submit = SubmitField('Request Password Reset')
        
    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first()
        if user is None:
            raise ValidationError('There is no account with that email. You must register first.')

class ResetPasswordForm(FlaskForm):

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
        'Reset Password'
    )

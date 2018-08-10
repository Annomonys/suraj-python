from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from surajpython.models import User


class RegistrationForm(FlaskForm):
    fullname = StringField('Fullname',
                validators= [DataRequired(), Length(min=2, max=50)])
    email = StringField('Email', 
                validators= [DataRequired(), Email()])
    password = PasswordField('Password', validators= [DataRequired()])
    confirm_password = PasswordField('Confirm Password', 
                validators= [DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_field(self, fullname):
        
        user = User.query.filter_by(fullname = fullname.data).first()
        if user:
            raise ValidationError('That fullname is taken. Please Choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first()
        if user:
            raise ValidationError ('The email is taken. Please choose a differnt one')

class LoginForm(FlaskForm):
    email = StringField('Email',
                validators= [DataRequired(), Email()])
    password = PasswordField('Password', validators= [DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    fullname = StringField('fullname',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_fullname(self, fullname):
        if fullname.data != current_user.fullname:
            user = User.query.filter_by(fullname=fullname.data).first()
            if user:
                raise ValidationError('That Username is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')

class PostForm(FlaskForm):
    title = StringField('Title', validators = [DataRequired()])
    content = TextAreaField('Content', validators = [DataRequired()])
    submit = SubmitField('Post')

class RequestResetForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first()
        if user is None:
            raise ValidationError('There is no account with that email. You must register first.')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators = [DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators = [DataRequired(), 
                                        EqualTo('password')])
    submit = SubmitField('Reset Password')
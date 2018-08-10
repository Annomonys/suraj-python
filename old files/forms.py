# from flask_wtf import Form
# from wtforms import StringField, PasswordField, SubmitField
# from wtforms.validators import DataRequired, Email, Length

# class SignupForm(Form):
#     first_name = StringField('First name', validators = [DataRequired("Please enter your first name")])
#     last_name = StringField('Last name', validators = [DataRequired("Please enter your last name")])
#     email = StringField('Email', validators = [DataRequired("Please enter your email"), Email("Please Enter your email")])
#     password = PasswordField('Password', validators = [DataRequired("Please enter your password"),Length(min=6, message="Password must be atlease 6 character")])
#     submit = SubmitField('Sign up')

# class LoginForm(Form):
#     email = StringField('Email', validators=[DataRequired("please enter your email address"), Email("Please enter your email")])
#     password = PasswordField('Password', validators = [DataRequired("Please enter your password"),Length(min=6, message="Password must be atlease 6 character")])
#     submit = SubmitField("Sign in")

# class AddressForm(Form):
#     address = StringField('Address', validators= [DataRequired('Please enter the address')])
#     submit = SubmitField("Search")

# class Reset(Form):
#     email = StringField('Email', validators=[DataRequired("please enter your email address"), Email("Please enter your email")])
#     submit = SubmitField("Submit")



from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    fullname = StringField('Fullname',
                validators= [DataRequired(), Length(min=2, max=50)])
    email = StringField('Email', 
                validators= [DataRequired(), Email()])
    password = PasswordField('Password', validators= [DataRequired()])
    confirm_password = PasswordField('Confirm Password', 
                validators= [DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email',
                validators= [DataRequired(), Email()])
    password = PasswordField('Password', validators= [DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

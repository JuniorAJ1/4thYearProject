from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo

# the wtf flask libary allows us to put validatos on our user inputs for example if there is no @ on a email 

class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(), Length(min = 2, max = 20)])
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('CPassword', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign up')
    
class SigninForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember')
    submit = SubmitField('Sign in')
    



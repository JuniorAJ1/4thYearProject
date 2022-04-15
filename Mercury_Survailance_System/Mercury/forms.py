from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from Mercury.database import User


# the wtf flask libary allows us to put validatos on our user inputs for example if there is no @ on a email 

class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(), Length(min = 2, max = 20)])
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign up')
    
    def validate_name(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('this Username has already beein used')
        
    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('this Email has already beein used')
    
class SigninForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember')
    submit = SubmitField('Sign in')
    



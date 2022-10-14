import email
from email import message
from xml.dom import ValidationErr
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,fields, FormField , EmailField
from wtforms.validators import DataRequired, Length, Email, EqualTo, email_validator, ValidationError
import email_validator
from flaskblog.models import User


class Registration_form(FlaskForm):
    
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exist, try a different username')
    def validate_email(self, email_to_check):
        user = User.query.filter_by(email=email_to_check.data).first()
        if user:
            raise ValidationError('Email already exist, try a different email')

    username = StringField('Username', validators=[DataRequired(), Length(min=3)])
    email = EmailField('Your Email', validators=[DataRequired(), Email()])
    password1 = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Confirm Password', validators=[EqualTo('password1')])
    submit = SubmitField('Sign-Up')
    

class Login_form(FlaskForm):
       
    email = EmailField('Email', validators=[DataRequired(), Email()])
    
    password = PasswordField('Password', validators=[DataRequired()])
    
    remember = BooleanField('Remember Me')
    
    submit = SubmitField('Login')
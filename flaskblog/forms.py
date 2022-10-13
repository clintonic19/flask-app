import email
from email import message
from xml.dom import ValidationErr
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,fields, FormField
from wtforms.validators import DataRequired, Length, Email, EqualTo, email_validator, ValidationError
import email_validator
from flaskblog.models import User


class Registration_form(FlaskForm):
    
    username = StringField(label='Username', validators=[DataRequired(), Length(min=2, max=20)]),
    
    email = StringField(label='Email', validators=[DataRequired(), Email()]),
    
    password = PasswordField(label='Password', validators=[DataRequired()]),
    
    confirm_password = PasswordField(label='Confirm Password', validators=[DataRequired(), EqualTo('password')])
    
    submit = SubmitField('Sign Up')
    
    
    def validate_username(self, username):
        
        user=User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exist', 'danger')
    
    def validate_email(self, email):
        
        user=User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already exist', 'danger')
    

class Login_form(FlaskForm):
       
    email = StringField(label='Email', validators=[DataRequired(), Email()]),
    
    password = PasswordField(label='Password', validators=[DataRequired()]),
    
    remember = BooleanField('Remember Me')
    
    submit = SubmitField('Login')
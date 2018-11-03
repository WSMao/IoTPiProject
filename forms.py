from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class LoginForm(FlaskForm):
    
    email = StringField('Email',
        validators=[DataRequired(), Email()] )
    password = PasswordField('Password', 
        validators=[DataRequired()])
    # using cookies
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
    




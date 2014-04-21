from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, BooleanField
from wtforms.validators import Required, Email, EqualTo, Length


class LoginForm(Form):
	email = TextField('Email Address', [Email(), Required(message='Please enter a valid email address')])
	password = PasswordField('Password', [Required(message='Please enter a password')])


class RegisterForm(Form):
	email = TextField('Email Address', [Email(), 
		Required(message='Please enter a valid email address')])
	password = PasswordField('Password', [
		Required(message='Please enter a password'), 
		Length(min=6, max=26, message='Password must be between %(min)d and %(max)d characters')])
	confirm_password = PasswordField('Confirm Password', [
		Required(message='Please confirm your password'), 
		EqualTo(fieldname='password', message='Passwords must match'),
		Length(min=6, max=26, message='Password must be between %(min)d and %(max)d characters')])
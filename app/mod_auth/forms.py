from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, BooleanField
from wtforms.validators import Required, Email, EqualTo


class LoginForm(Form):
	email = TextField('Email Address', [Email(), Required(message='Please enter a valid email address')])
	password = PasswordField('Password', [Required(message='Please enter a password')])


class RegisterForm(Form):
	email = TextField('Email Address', [Email(), Required(message='Please enter a valid email address')])
	password = PasswordField('Password', [Required(message='Please enter a password')])
	confirm_password = PasswordField('Confirm Password', [Required(message='Passwords must match')])
from flask import abort, Blueprint, request, render_template, flash, g, \
	session, redirect, url_for
from werkzeug import check_password_hash, generate_password_hash

from app import db
from app.mod_auth.forms import LoginForm, RegisterForm
from app.mod_auth.models import User


# Define the blueprint
mod_auth = Blueprint('auth', __name__, url_prefix='/auth')

@mod_auth.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm(request.form)
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user and check_password_hash(user.password, form.password.data):
			session['user_id'] = user.id
			flash('Welcome %s' % user.username)
			redirect(url_for('auth.home'))
		flash('Incorrect email or password', 'error')
	return render_template('mod_auth/login.html', form=form)

@mod_auth.route('/register', methods=['GET', 'POST'])
def register():
	form = RegisterForm(request.form)
	return render_template('mod_auth/register.html', form=form)
	# if form.validate_on_submit():
	# 	user = User(username=form.email.data, email=form.email.data, password=form.password.data)
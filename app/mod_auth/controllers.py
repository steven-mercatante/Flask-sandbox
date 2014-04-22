from flask import abort, Blueprint, request, render_template, flash, g, \
	session, redirect, url_for
from flask.ext.login import login_user, logout_user, current_user, \
	login_required
from werkzeug import check_password_hash, generate_password_hash

from app import app, db, login_manager
from app.mod_auth.forms import LoginForm, RegisterForm
from app.mod_auth.models import User


# Define the blueprint
mod_auth = Blueprint('auth', __name__, url_prefix='/auth')

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(user_id)

@app.before_request
def before_request():
	g.user = current_user

@mod_auth.route('/profile')
@login_required
def profile():
	return render_template('mod_auth/profile.html', user=g.user)

@mod_auth.route('/register', methods=['GET', 'POST'])
def register():
	form = RegisterForm(request.form)
	if form.validate_on_submit():
		username = form.email.data
		email = form.email.data
		password = form.password.data
		confirm_password = form.confirm_password.data
		if not email or not password:
			flash('Please provide an email address and password', 'error')
			return redirect(url_for('auth.register'))
		if User.query.filter_by(email=email).first():
			flash('That user account already exists', 'error')
			return redirect(url_for('auth.register'))
		user = User(username=email, email=email, password=generate_password_hash(password))
		db.session.add(user)
		db.session.commit()
		login_user(user)
		return redirect(url_for('auth.profile'))
	return render_template('mod_auth/register.html', form=form)

@mod_auth.route('/login', methods=['GET', 'POST'])
def login():
	if g.user is not None and g.user.is_authenticated():
		return redirect(url_for('auth.profile'))
	form = LoginForm(request.form)
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user and check_password_hash(user.password, form.password.data):
			session['user_id'] = user.id
			return redirect(url_for('auth.profile'))
		else:
			flash('Incorrect email or password', 'error')
			return redirect(url_for('auth.login'))
	return render_template('mod_auth/login.html', form=form)

@mod_auth.route('/logout')
def logout():
	if g.user is None or g.user.is_authenticated() == False:
		return redirect(url_for('auth.profile'))
	logout_user()
	return redirect(url_for('auth.login'))

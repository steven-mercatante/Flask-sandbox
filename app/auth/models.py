from datetime import datetime
import hashlib

from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app, request, url_for
from flask.ext.login import UserMixin, AnonymousUserMixin

from app.exceptions import ValidationError
from .. import db, login_manager

ROLE_USER = 0
ROLE_ADMIN = 1

STATUS_PENDING = 0
STATUS_APPROVED = 1
STATUS_BANNED = 2

class Base(db.Model):
	__abstract__ = True

	id = db.Column(db.Integer, primary_key=True)
	date_created = db.Column(db.DateTime, default=datetime.utcnow)
	date_updated = db.Column(db.DateTime, default=datetime.utcnow) 


class User(Base):
	__tablename__ = 'user'

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(128), nullable=False)
	email = db.Column(db.String(128), nullable=False, unique=True)
	password_hash = db.Column(db.String(128), nullable=False)
	role = db.Column(db.SmallInteger, nullable=False, default=ROLE_USER)
	status = db.Column(db.SmallInteger, nullable=False, default=STATUS_PENDING)
	confirmed = db.Column(db.Boolean, default=False)
	last_seen = db.Column(db.DateTime(), default=datetime.utcnow)

	def __init__(self, username, email, password):
		self.username = username
		self.email = email
		self.password = password

	@property
	def password(self):
		raise AttributeError('password is not a readable attribute')

	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		return check_password_hash(password)

	def generate_confirmation_token(self, expiration=3600):
		s = Serializer(current_app.config['SECRET_KEY'], expiration)
		return s.dumps({'confirm': self.id})

	def confirm(self, token):
		s = Serializer(current_app.config['SECRET_KEY'])
		try:
		    data = s.loads(token)
		except:
		    return False
		if data.get('confirm') != self.id:
		    return False
		self.confirmed = True
		db.session.add(self)
		return True

	def generate_reset_token(self, expiration=3600):
		s = Serializer(current_app.config['SECRET_KEY'], expiration)
		return s.dumps({'reset': self.id})

	def reset_password(self, token, new_password):
		s = Serializer(current_app.config['SECRET_KEY'])
		try:
		    data = s.loads(token)
		except:
		    return False
		if data.get('reset') != self.id:
		    return False
		self.password = new_password
		db.session.add(self)
		return True

	def generate_email_change_token(self, new_email, expiration=3600):
		s = Serializer(current_app.config['SECRET_KEY'], expiration)
		return s.dumps({'change_email': self.id, 'new_email': new_email})

	def change_email(self, token):
		s = Serializer(current_app.config['SECRET_KEY'])
		try:
		    data = s.loads(token)
		except:
		    return False
		if data.get('change_email') != self.id:
		    return False
		new_email = data.get('new_email')
		if new_email is None:
		    return False
		if self.query.filter_by(email=new_email).first() is not None:
		    return False
		self.email = new_email
		self.avatar_hash = hashlib.md5(
		    self.email.encode('utf-8')).hexdigest()
		db.session.add(self)
		return True

	def ping(self):
		self.last_seen = datetime.utcnow()
		db.session.add(self)

	def is_authenticated(self):
		if self.username:
			return True
		return False

	def is_active(self):
		return self.is_actived

	def is_anonymous(self):
		if self.username:
			return False
		return True

	def get_id(self):
		return unicode(self.id)

	def __repr__(self):
		return '<User %r>' % self.username


class AnonymousUser(AnonymousUserMixin):
    def can(self, permissions):
        return False

    def is_administrator(self):
        return False
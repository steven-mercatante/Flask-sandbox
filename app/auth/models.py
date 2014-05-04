from app import db
from werkzeug.security import generate_password_hash, check_password_hash

ROLE_USER = 0
ROLE_ADMIN = 1

STATUS_PENDING = 0
STATUS_APPROVED = 1
STATUS_BANNED = 2

class Base(db.Model):
	__abstract__ = True

	id = db.Column(db.Integer, primary_key=True)
	date_created = db.Column(db.DateTime)
	date_updated = db.Column(db.DateTime) 


class User(Base):
	__tablename__ = 'user'

	username = db.Column(db.String(128), nullable=False)
	email = db.Column(db.String(128), nullable=False, unique=True)
	password_hash = db.Column(db.String(128), nullable=False)
	role = db.Column(db.SmallInteger, nullable=False, default=ROLE_USER)
	status = db.Column(db.SmallInteger, nullable=False, default=STATUS_PENDING)
	is_activated = db.Column(db.SmallInteger, nullable=False, default=0)

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

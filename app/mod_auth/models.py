from app import db

ROLE_USER = 0
ROLE_ADMIN = 1

STATUS_PENDING = 0
STATUS_APPROVED = 1
STATUS_BANNED = 2

class Base(db.Model):
	__abstract__ = True

	id = db.Column(db.Integer, primary_key=True)
	date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
	date_updated = db.Column(db.DateTime, default=db.func.current_timestamp(), 
		onupdate=db.func.current_timestamp())


class User(Base):
	__tablename__ = 'auth_user'

	username = db.Column(db.String(128), nullable=False)
	email = db.Column(db.String(128), nullable=False, unique=True)
	password = db.Column(db.String(128), nullable=False)
	role = db.Column(db.SmallInteger, nullable=False, default=ROLE_USER)
	status = db.Column(db.SmallInteger, nullable=False, default=STATUS_PENDING)

	def __init__(self, username, email, password):
		self.username = username
		self.email = email
		self.password = password

	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return unicode(self.id)

	def __repr__(self):
		return '<User %r>' % self.username

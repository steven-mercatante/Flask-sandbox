from app import db

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
	__tablename__ = 'auth_user'

	username = db.Column(db.String(128), nullable=False)
	email = db.Column(db.String(128), nullable=False, unique=True)
	email2 = db.Column(db.String(128), nullable=False, unique=True)
	password = db.Column(db.String(128), nullable=False)
	role = db.Column(db.SmallInteger, nullable=False, default=ROLE_USER)
	status = db.Column(db.SmallInteger, nullable=False, default=STATUS_PENDING)
	is_activated = db.Column(db.SmallInteger, nullable=False, default=0)

	def __init__(self, username, email, password):
		self.username = username
		self.email = email
		self.password = password

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

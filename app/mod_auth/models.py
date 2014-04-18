from app import db


class Base(db.Model):
	__abstract__ = True

	id = db.Column(db.Integer, primary_key=True)
	date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
	date_updated = db.Column(db.DateTime, default=db.func.current_timestamp())

onupdate = db.func.current_timestamp()

class User(Base):
	__table__name = 'auth_user'

	username = db.Column(db.String(128), nullable=False)
	email = db.Column(db.String(128), nullable=False, unique=True)
	password = db.Column(db.String(128), nullable=False)

	role = db.Column(db.SmallInteger, nullable=False)
	status = db.Column(db.SmallInteger, nullable=False)

	def __init__(self, username, email, password):
		self.username = username
		self.email = email
		self.password = password

	def __repr__(self):
		return '<User %r>' % self.username
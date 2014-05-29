from datetime import datetime

from . import db

class Base(db.Model):
	__abstract__ = True

	id = db.Column(db.Integer, primary_key=True)
	date_created = db.Column(db.DateTime, default=datetime.utcnow)
	date_updated = db.Column(db.DateTime, default=datetime.utcnow) 
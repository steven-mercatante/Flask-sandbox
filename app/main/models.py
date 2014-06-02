from .. import db
from .. models import Base

# class Person(Base):
# 	__tablename__ = 'person'

# 	first_name = db.Column(db.String(60))
# 	last_name = db.Column(db.String(60))

# 	def __init__(self, first_name, last_name):
# 		self.first_name = first_name
# 		self.last_name = last_name

# 	def __repr__(self):
# 		return '<Person %s %s>' % (self.first_name, self.last_name)
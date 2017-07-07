from fll import db
from sqlalchemy.dialects.postgresql import JSON

class Task(db.Model):
	__tablename__ = 'tasks'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100))

	def __init__(self, name):
		self.name = name

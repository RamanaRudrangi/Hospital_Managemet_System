from app import db
from datetime import datetime

class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    specialization_id = db.Column(db.Integer, db.Foreignkey('departments.id'),nullabale=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    role = db.Column(db.String(50), default=datetime.utcnow)


class Department(db.Model):
    __tablename__='departments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)

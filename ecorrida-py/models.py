from config import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    education_level = db.Column(db.String(100), nullable=True)  # nullable=True permite valores nulos
    gender = db.Column(db.String(20), nullable=True)  # nullable=True permite valores nulos

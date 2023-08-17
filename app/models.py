from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from random import randint
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(75), nullable=False, unique=True)
    username = db.Column(db.String(75), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    posts = db.relationship('Phone', backref='author')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.password = generate_password_hash(kwargs.get('password'))

    def __repr__(self):
        return f"<User {self.id}|{self.username}>"
    
    def check_password(self, password_guess):
        return check_password_hash(self.password, password_guess)

@login.user_loader
def load_user(user_id):
    return db.session.get(User, user_id)

class Phone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(75), nullable=False, unique=True)
    phoneNum = db.Column(db.String(75), nullable=False, unique=True)
    dateCreated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)  # SQL - FOREIGN KEY(user_id) REFERENCES user(id)

    def __repr__(self):
        return f"<User {self.id}|{self.first_name} {self.last_name}>"

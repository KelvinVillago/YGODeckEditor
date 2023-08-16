from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(75), nullable=False, unique=True)
    phoneNum = db.Column(db.String(75), nullable=False, unique=True)
    dateCreated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


    def __repr__(self):
        return f"<User {self.id}|{self.first_name} {self.last_name}>"


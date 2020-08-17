from notefy import db
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

import time

class User(UserMixin, db.Model):
    
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(40), nullable=False)
    username = db.Column(db.String(40), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    rank = db.Column(db.String(20), default='User')
    verify_key = db.Column(db.String(40), default=False)
    register_time = db.Column(db.Float(), default=time.time())

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = generate_password_hash(password)
        self.verify_key = generate_password_hash(username + str(time.time()))

db.create_all()

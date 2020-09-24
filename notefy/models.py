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
    subjects = db.Column(db.String(128), nullable=False)

    def __init__(self, username, email, password, subjects):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.subjects = subjects
        self.verify_key = generate_password_hash(username + str(time.time()))

class Note(db.Model):

    __tablename__ = 'note'
    id = db.Column(db.Integer, primary_key=True)
    file_path = db.Column(db.String(40), nullable=False)
    subject = db.Column(db.String(40), nullable=False)
    topics = db.Column(db.String(128), nullable=False)


    def __init__(self, subject, topics):
        pass

    def get_path(self):
        pass

db.create_all()

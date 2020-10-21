from notefy import db
from notefy.subject_info import subject_dict

from flask_login import UserMixin
from werkzeug.security import generate_password_hash

import time
import os
import json


class User(UserMixin, db.Model):

    __tablename__ = 'user'

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
    subject = db.Column(db.String(40), nullable=False)
    topics = db.Column(db.String(128), nullable=False)
    file_ext = db.Column(db.String(10), nullable=False)

    likes = db.Column(db.Integer, default=0)
    favorites = db.Column(db.Integer, default=0)

    liked_users_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    favorite_users_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    owner_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    liked_users = db.relationship(
        "User",
        backref="liked_notes",
        foreign_keys=[liked_users_id],
        uselist=True
    )
    favorite_users = db.relationship(
        "User",
        backref="favorite_notes",
        foreign_keys=[favorite_users_id],
        uselist=True
    )
    owner = db.relationship(
        "User", backref="owned_notes", foreign_keys=[owner_id]
    )

    def __init__(self, subject, topics, file_ext, owner: User,):
        self.subject = subject
        self.topics = topics
        self.file_ext = file_ext
        self.owner = owner

    def get_file_path(self):
        dirname = os.path.dirname(__file__)
        return os.path.join(
            dirname,
            "uploads/notes",
            str(self.id) + "." + self.file_ext
        )

    def get_subject_object(self):
        return subject_dict.get(self.subject)

    def get_topics_as_string(self):
        return ", ".join(json.loads(self.topics))


db.create_all()

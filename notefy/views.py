from notefy import app, db, login_manager
from notefy.models import User

from flask import render_template, request, redirect, url_for, jsonify
from werkzeug.security import generate_password_hash

@app.route("/")
def home():
	return render_template("home.html", title="Notefy: Home")

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(user_id)

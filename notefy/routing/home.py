from notefy import app
from notefy.models import User

from flask import render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_user, current_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_
from werkzeug.security import check_password_hash


import json

@app.route("/")
def home():
    if current_user.is_authenticated:
        return redirect(url_for("notes"))
    return render_template("home.html", title="Notefy: Home")

@app.route("/login", methods=['POST'])
def login():
    if request.method == "POST":
        # TODO: Data Validation
        user_data = json.loads(request.form["data"]).get("user")
        username = user_data.get("username")
        matched_user = User.query.filter(or_(User.username==username, User.email==username)).first()
        if check_password_hash(matched_user.password, user_data.get("password")):
            login_user(matched_user)
            return jsonify({"login": "success"})
        return render_template("login.html", title="Nope")
        

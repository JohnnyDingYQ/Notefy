from notefy import app
from notefy.models import User

from flask import render_template, flash, redirect, url_for
from flask_login import login_user, current_user
from sqlalchemy import func
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired

from werkzeug.security import check_password_hash


class LoginForm(FlaskForm):
    username = StringField(
        "Username or Email Address",
        validators=[InputRequired("Username cannot be empty")]
    )
    password = PasswordField(
        "Password",
        validators=[InputRequired("Password cannot be empty")]
    )


@app.route("/")
def home():
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for("notes"))
    return render_template("home.html", title="Notefy: Home", form=form)


@app.route("/login", methods=['POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # TODO: Data Validation
        username = form.username.data.lower()
        matched_user = User.query.filter(
            (func.lower(User.username) == username) |
            (func.lower(User.email) == username)
        ).one_or_none()
        if check_password_hash(matched_user.password, form.password.data):
            login_user(matched_user)
            flash("Login success", "flash-info")
            return redirect(url_for("notes"))
    return render_template("home.html", title="Notefy: Home", form=form)

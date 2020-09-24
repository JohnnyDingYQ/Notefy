from notefy import app, db
from notefy.models import User
from notefy.subject_info import subject_dict

from flask import render_template, request, flash, url_for, redirect, abort
from flask_login import login_user

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, EqualTo, Email

import json


class RegistrationForm(FlaskForm):
    username = StringField(
        "Username", validators=[InputRequired("Username can not be empty")]
    )
    email = StringField(
        "Email", validators=[
            InputRequired("Email can not be empty"),
            Email("Wrong Email Format")
        ]
    )
    password = PasswordField(
        "Password",
        validators=[
            InputRequired("Password can not be empty"),
            EqualTo("confirm_password", "Password does not match")
        ]
    )
    confirm_password = PasswordField(
        'Confirm Password',
        validators=[InputRequired("Please confirm your password")]
    )


for key, item in subject_dict.items():
    setattr(RegistrationForm, key, BooleanField(item.display_text))


@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = RegistrationForm()
    if request.method == "POST":
        if form.validate_on_submit():
            checked_subjects = [i.id for i in form if i.data is True]
            if len(checked_subjects) != 6:
                abort(404)
            new_user = User(
                form.username.data,
                form.email.data,
                form.password.data,
                json.dumps(checked_subjects)
            )

            db.session.add(new_user)
            db.session.commit()

            login_user(new_user)
            flash("Sign up success")

            return redirect(url_for("notes"))

    return render_template("signup.html", title="Sign up", form=form)

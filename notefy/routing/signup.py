from notefy import app, db
from notefy.models import User

from flask import render_template, request, flash
from flask_login import login_user
from werkzeug.security import generate_password_hash

import json

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        user_data = json.loads(request.form["data"]).get("user")
        # TODO: Data Validation
        new_user = User(
            user_data.get("username"),
            user_data.get("email"),
            user_data.get("password"),
            json.dumps(user_data.get("subjects"))
        )
        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)
        flash("Sign up success")
        
        return render_template("notes.html", title="Notefy")


    return render_template("signup.html", title="Sign up")

from notefy import app

from flask import render_template

@app.route("/signup")
def signup():
    return render_template("signup.html", title="Sign up")
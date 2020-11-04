from notefy import app, db

from flask import render_template
from flask_login import login_required
from flask_wtf import FlaskForm
from wtforms import PasswordField
from wtforms.validators import InputRequired, EqualTo, Length


class ResetPasswordForm(FlaskForm):
    old_password = PasswordField(
        "Old Password",
        validators=[InputRequired("Old password cannot be empty")]
    )
    new_password = PasswordField(
        "New Password",
        validators=[
            InputRequired("New password cannot be empty"),
            EqualTo("confirm_new_password", "Password does not match"),
            Length(8, 64, "Password should be between 8 and 64 characters")
        ],
    )
    confirm_new_password = PasswordField(
        "New Password",
        validators=[InputRequired("Confirm your new password")]
    )


@login_required
@app.route("/reset_password", methods=["GET"])
def reset_password():
    form = ResetPasswordForm()
    return render_template(
        "reset_password.html",
        title="Reset Password",
        form=form
    )

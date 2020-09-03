from notefy import app

from flask import render_template, request, abort
from flask_login import login_required, current_user

import json
import os

@app.route("/notes")
@login_required
def notes():
    user_subjects = json.loads(current_user.subjects)

    f = open(os.path.dirname(__file__) + '/../subject-info.json')
    subject_info = json.load(f)
    f.close()

    if request.args.get("subject"):
        subject = request.args.get("subject")
        if subject not in user_subjects:
            return abort(404)
        subject_display_name = subject_info.get(subject).get("display_text")
    else:
        subject = None
        subject_display_name = None

    if request.args.get("subject"):
        folder = request.args.get("folder")
    else:
        folder = None
    
    if not subject and folder:
        return abort(404)

    display_text = []
    for s in user_subjects:
         display_text.append(subject_info.get(s).get("display_text"))
    user_subjects = zip(user_subjects, display_text)
    
    # TODO: Determine if reading json for every request is too memory intensive

    return render_template(
        "notes.html",
        title="Notefy",
        user_subjects=list(user_subjects),
        subject=subject,
        subject_display_name=subject_display_name,
        folder=folder,
    )
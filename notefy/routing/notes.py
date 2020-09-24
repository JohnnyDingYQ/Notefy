from notefy import app
from notefy.subject_info import subject_dict

from flask import render_template, request, abort, jsonify
from flask_login import login_required, current_user

import json
import os


@app.route("/notes")
@login_required
def notes():
    subjects = json.loads(current_user.subjects)

    user_subjects = [subject_dict.get(i) for i in subjects]

    if request.args.get("subject"):
        subject = request.args.get("subject")
        if request.args.get("subject") not in subjects:
            return abort(404)
        subject = subject_dict.get(subject)
    else:
        subject = None

    if request.args.get("subject"):
        folder = request.args.get("folder")
    else:
        folder = None

    if not subject and folder:
        return abort(404)

    return render_template(
        "notes.html",
        title="Notefy",
        user_subjects=list(user_subjects),
        subject=subject,
        folder=folder,
    )


@app.route("/upload_notes", methods=["POST"])
@login_required
def upload_notes():
    note_file = request.files.getlist("file")
    note_topics = request.form["topics"].split(",")
    note_subject = request.form["subject"]
    print(note_file)

    if note_subject not in subject_dict.keys():
        return jsonify({"code": 1})
    else:
        subject = subject_dict.get(note_subject)
        for t in note_topics:
            if t not in subject.topics:
                return jsonify({"code": 2})
    return jsonify({"code": 0})

from notefy import app, db
from notefy.subject_info import subject_dict
from notefy.helper import allowed_file
from notefy.models import Note

from flask import (
    render_template,
    request,
    abort,
    jsonify,
    send_file,
    flash
)
from flask_login import login_required, current_user

import json
import os
import re
import urllib.parse


@app.route("/notes")
@login_required
def notes():
    subjects = json.loads(current_user.subjects)

    user_subjects = [subject_dict.get(i) for i in subjects]

    notes = Note.query.filter(Note.subject.in_(subjects))

    if request.args.get("subject"):
        subject = request.args.get("subject")
        if request.args.get("subject") not in subjects:
            return abort(404)
        subject = subject_dict.get(subject)
        notes = notes.filter(Note.subject == subject.name)
    else:
        subject = None

    if request.args.get("subject_filter"):
        subject_filter = urllib.parse.unquote(
            request.args.get("subject_filter")
        )
        notes = notes.filter(Note.subject == subject_filter)
        filtered_subject = subject_dict.get(subject_filter)
    else:
        filtered_subject = None

    if request.args.get("folder"):
        folder = request.args.get("folder")
        if folder == "favorite":
            notes = notes.filter(Note.favorite_users.any(id=current_user.id))
    else:
        folder = None

    if request.args.get("my_notes_only"):
        notes = notes.filter(Note.owner == current_user)

    notes = notes.all()

    if request.args.get("topic_filter"):
        topic_filter = urllib.parse.unquote(request.args.get("topic_filter"))
        notes = [n for n in notes if topic_filter in json.loads(n.topics)]
    if not subject and folder:
        return abort(404)

    return render_template(
        "notes.html",
        title="Notefy",
        user_subjects=list(user_subjects),
        subject=subject,
        folder=folder,
        notes=notes,
        filtered_subject=filtered_subject
    )


@app.route("/upload_notes", methods=["POST"])
@login_required
def upload_notes():
    if request.files.getlist("file"):
        note_file = request.files.getlist("file")[0]
    else:
        return jsonify({"code": 3})
    note_topics = request.form["topics"].split(",")
    note_subject = request.form["subject"]

    if note_subject not in subject_dict.keys():
        return jsonify({"code": 1})
    else:
        subject = subject_dict.get(note_subject)
        for t in note_topics:
            if t not in subject.topics:
                return jsonify({"code": 2})
    if allowed_file(note_file.filename):
        new_note = Note(
            note_subject,
            json.dumps(note_topics),
            note_file.filename.rsplit('.', 1)[1].lower(),
            current_user
        )
        db.session.add(new_note)
        db.session.commit()
        dirname = os.path.dirname(__file__)
        note_file.save(
            os.path.join(
                dirname,
                "..",
                "..",
                app.config["UPLOAD_FOLDER"],
                "notes",
                str(new_note.id) + "." + note_file.filename.rsplit('.', 1)[1]
            )
        )
        note_file.close()
        return jsonify({"code": 0})
    return jsonify({"code": 4})


# note action specifically means likes and favorites
@app.route("/handle_note_action", methods=["POST"])
@login_required
def handle_note_action():
    note_id = int(re.findall(r"(?<=note_)\d*", request.form["note_id"])[0])
    action = request.form["action"]
    note = Note.query.filter_by(id=note_id).first()
    if action == "like":
        if current_user in note.liked_users:
            note.liked_users.remove(current_user)
            note.likes -= 1
            message = "un-liked"
        else:
            note.liked_users.append(current_user)
            note.likes += 1
            message = "liked"
    elif action == "favorite":
        if current_user in note.favorite_users:
            note.favorite_users.remove(current_user)
            note.favorites -= 1
            message = "un-favorite"
        else:
            note.favorite_users.append(current_user)
            note.favorites += 1
            message = "favorite"
    else:
        abort(404)
    db.session.commit()
    return jsonify({"message": message})


@app.route("/download_note", methods=["GET"])
@login_required
def download_note():
    note_id = int(re.findall(r"(?<=note_)\d*", request.args.get("note_id"))[0])
    note = Note.query.filter_by(id=note_id).first()
    return send_file(
        "uploads" + "/notes/" + str(note.id) + "." + note.file_ext
    )


@app.route("/delete_note", methods=["POST"])
@login_required
def delete_note():
    note_id = request.form["note_id"]
    note = Note.query.filter_by(id=note_id).one()
    if note.owner == current_user:
        d = os.path.dirname(__file__)
        path = d + "/../uploads/notes/" + str(note.id) + "." + note.file_ext
        if os.path.isfile(path):
            os.remove(path)
            db.session.delete(note)
            db.session.commit()
            return jsonify({"code": 1})
    else:
        return jsonify({"code": 2})
    return jsonify({"code": 3})

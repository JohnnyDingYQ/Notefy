from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from config import config


app = Flask(__name__)
app.secret_key = '+b^s|16!M.>"~SD*@'
app.config.from_object(config)

UPLOAD_FOLDER = '/notefy/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'docx', 'pptx'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db = SQLAlchemy(app)
db.app = app
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

from notefy import routing

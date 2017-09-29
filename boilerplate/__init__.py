from flask import Flask
from .database import db

app = Flask(__name__)
app.config.from_pyfile('../config.py')
app.config.from_pyfile('../instance/config.py')
from . import views
db.init_app(app)

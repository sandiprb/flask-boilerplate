from boilerplate import app
from boilerplate.database import db
import flask

def create_app():
    app = flask.Flask("app")
    app.config.from_pyfile('instance/config.py')
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app
create_app()

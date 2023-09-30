import os

from flask import Flask

from api.db import db
from api.routes import classify_api, user_api, access_token_api


BASE_DIR = os.path.dirname(__name__)
DATABASE = os.path.join(os.path.abspath(BASE_DIR), "user.db")

def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "secret"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DATABASE}"

    db.init_app(app)

    app.register_blueprint(classify_api)
    app.register_blueprint(user_api)
    app.register_blueprint(access_token_api)

    from api.model import User

    with app.app_context():
        if not os.path.isfile(DATABASE):
            db.create_all()

    return app


    
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .routes.routes import routesBlueprint
from .db.db import db


def create_app(settings):

    app = Flask(__name__)
    # app config
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
    # initialize the app with the extension
    db.init_app(app)

    # Blueprints

    app.register_blueprint(routesBlueprint)

    with app.app_context():
        pass
    return app

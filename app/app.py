from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .routes.routes import routesBlueprint
from .database.db import db

app = Flask(__name__)
# app config
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable tracking for performance

# initialize the app with the extension
db.init_app(app)


with app.app_context():
    db.create_all()

# Blueprints (general endpoints)

app.register_blueprint(routesBlueprint)

if __name__ == '__main__':
    app.run(debug=True)



from flask import Flask
from .routes.routes import routesBlueprint

def create_app(settings):
    
    app = Flask(__name__)
    # app config
    
    # Blueprints
    
    app.register_blueprint(routesBlueprint)
    
    with app.app_context():
        pass
    return app
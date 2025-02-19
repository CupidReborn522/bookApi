from flask import Flask

def create_app(settings):
    app = Flask(__name__)
    # app config
    
    # Blueprints
    app.register_blueprint()
    
    with app.app_context():
        pass
    return app
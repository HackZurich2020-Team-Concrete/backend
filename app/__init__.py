from flask import Flask
from flask_cors import CORS

def create_app():
    # initialize flask app and configure
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')

    # enable CORS
    CORS(app)

    # add all blueprints
    from .api import api_bp
    app.register_blueprint(api_bp)

    return app

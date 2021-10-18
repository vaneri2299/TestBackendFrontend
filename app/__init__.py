from flask import Flask
from app.utils import register_blueprints

def create_app():

    # Instanciar aplicacion de flask
    app = Flask(__name__)

    register_blueprints(app)

    return app
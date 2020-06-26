from flask import Flask
from config import config_options

def create_app(config_name):
    '''
    Function to start up the application
    '''
    app = Flask(__name__)

    # Setting the config
    app.config.from_object(config_options[config_name])

    # Registering Blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/v1')

    return app




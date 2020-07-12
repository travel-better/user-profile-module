from flask import Flask
from config import config_options
import flask_injector
from flaskext.couchdb import CouchDBManager
from app.models import UserProfile

INJECTOR_DEFAULT_MODULES = dict(
    db_manager=CouchDBManager,
)

def create_app(config_name, **kwargs):
    '''
    Application entry point
    '''
    app = Flask(__name__)

    # Setting the config
    app.config.from_object(config_options[config_name])

    # Registering Blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/api/v1')

    # Initializing couchdb manager
    couch = CouchDBManager()
    couch.add_document(UserProfile)
    couch.setup(app)

    # Injecting db manager module
    flask_injector.FlaskInjector(app=app, modules=INJECTOR_DEFAULT_MODULES.values())

    return app




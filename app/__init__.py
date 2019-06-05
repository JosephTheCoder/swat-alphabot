from flask import Flask
from config import config, Config
from flask_migrate import Migrate
from flask_cors import CORS
from app.database import db, create_tables
from flask_login import LoginManager
import logging
import os


def initialize_auth_api_blueprint(app):
    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

def initialize_robot_control_api(app):
    from app.robot_control import bp as robot_control_bp
    app.register_blueprint(robot_control_bp)

def initialize_video_stream_api(app):
    from app.video_stream import bp as video_stream_bp
    app.register_blueprint(video_stream_bp)


def create_app():
    app = Flask(__name__)

    env_config = Config.APP_ENV
    app.config.from_object(config[env_config])

    current_path = os.path.dirname(os.path.realpath(__file__))

    migrations_dir = os.path.join(current_path, 'database', 'migrations')
    Migrate(app, db, directory=migrations_dir)
   
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    from app.models.users import Users

    @login_manager.user_loader
    def load_user(uuid):
        user = Users.query.filter_by(uuid=uuid).first()
        if user is None:
            return None
        return user

    @login_manager.unauthorized_handler
    def unauthorized_handler():
        return 'Unauthorized'

    with app.app_context():
        db.init_app(app)
        create_tables()

    CORS(app) # enable Cross-Origin Resource Sharing
    
    initialize_auth_api_blueprint(app)
    #initialize_robot_control_api(app)
    #initialize_video_stream_api(app)

    @app.shell_context_processor
    def make_shell_context():
        return {'db': db, 'User': Users}
    
    return app


# Setup logger -----------------------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


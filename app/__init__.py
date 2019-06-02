from flask import Flask
from config import config, Config
from flask_cors import CORS
import logging
import os
from flask_login import LoginManager


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

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    @login_manager.unauthorized_handler
    def unauthorized_handler():
        return 'Unauthorized'

    CORS(app) # enable Cross-Origin Resource Sharing
    
    initialize_auth_api_blueprint(app)
    initialize_robot_control_api(app)
    initialize_video_stream_api(app)
    
    return app


# Setup logger -----------------------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


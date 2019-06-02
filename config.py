import os
from os.path import join, dirname
from dotenv import load_dotenv

#TODO get the dotenv environment to work
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

class Config(object):
    # Default configuration
    APP_ENV = os.environ.get('APP_ENV', 'development')

    SECRET_KEY = os.environ.get('SECRET_KEY')

    ADMIN_USER = os.environ.get('ADMIN_USER')
    ADMIN_PASS = os.environ.get('ADMIN_PASS')
    
    DEBUG = True
    TESTING = False


class DevelopmentConfig(Config):
    """Development configuration"""
    SECRET_KEY = os.environ.get('SECRET_KEY')

    DEBUG = True
    TESTING = True
 

class TestingConfig(Config):
    """Testing configuration"""
    DEBUG = True
    TESTING = True


class StagingConfig(Config):
    """ Staging configuration"""
    DEBUG = True
    SESSION_COOKIE_SECURE = True
    DEVELOPMENT = True


class ProductionConfig(Config):
    """Production configuration"""
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = False
    SESSION_COOKIE_SECURE = True

config = {
    'development': DevelopmentConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}

__all__ = ['config']

import os
from dotenv import load_dotenv
load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """
    Base configuration class. Contains default configuration settings + configuration settings applicable to all environments.
    """
    # Default Settings
    DEBUG = False
    TESTING = False
    WTF_CSRF_ENABLED = True
    
    # Twitter Config
    BEARER_TOKEN = os.getenv('BEARER_TOKEN', default=None)
    
    # Settings applicable to all environments
    SECRET_KEY = os.getenv('SECRET_KEY', default='Its a trap')
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, 'default.db')
    
    
class DevelopmentConfig(Config):
    DEBUG = True
    
class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, 'test.db')
    
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, 'prod.db')
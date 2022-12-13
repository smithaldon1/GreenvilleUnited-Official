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
    
    
    
class DevelopmentConfig(Config):
    DEBUG = True
    API_LOGIN_ID = os.getenv('DEV_API_LOGIN_ID')
    TRANSACTION_KEY = os.getenv('DEV_TRANSACTION_KEY')
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, 'default.db')
    
class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, 'test.db')
    
class ProductionConfig(Config):
    MYSQL_USER = os.getenv('MARIADB_USER')
    MYSQL_PASSWORD = os.getenv('MARIADB_PASSWORD')
    MYSQL_HOST = os.getenv('MARIADB_HOST')
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/" + os.path.join(basedir, 'prod.db')
    API_LOGIN_ID = os.getenv('DEV_API_LOGIN_ID')
    TRANSACTION_KEY = os.getenv('DEV_TRANSACTION_KEY')
import os
import logging
from flask import Flask, render_template
from flask.logging import default_handler
from logging.handlers import RotatingFileHandler
from jinja2 import ChoiceLoader, FileSystemLoader


### Application Factory ### 
def create_app():
    app = Flask(__name__)
    
    # Configure Flask App Instance
    CONFIG_TYPE = os.getenv('CONFIG_TYPE', default='config.DevelopmentConfig')
    app.config.from_object(CONFIG_TYPE)
    
    # Register blueprints
    register_blueprints(app)
    
    # Initialize flask extension objects
    initialize_extensions(app)
    
    # Configure logging
    configure_logging(app)
    
    # Register error handlers
    register_error_handlers(app)
    
    # Overwrite Flask jinja_loader, using ChoiceLoader
    template_loader = ChoiceLoader([
        app.jinja_loader,
        FileSystemLoader('static'),
    ])
    
    return app
    
def register_blueprints(app):
    from app.about import about_bp
    from app.auth import auth_bp
    from app.community import community_bp
    from app.contact import contact_bp
    from app.main import main_bp
    from app.partners import partners_bp
    from app.store import store_bp
    
    app.register_blueprint(about_bp, url_prefix='/about')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(community_bp, url_prefix='/community')
    app.register_blueprint(contact_bp, url_prefix='/contact')
    app.register_blueprint(main_bp)
    app.register_blueprint(partners_bp, url_prefix='/partners')
    app.register_blueprint(store_bp, url_prefix='/store')
    
def initialize_extensions(app):
    pass

def register_error_handlers(app):
    # 400 – Bad Request
    @app.errorhandler(400)
    def bad_request(e):
        return render_template('400.html'), 400
    
    # 403 – Forbidden
    @app.errorhandler(403)
    def forbidden(e):
        return render_template('403.html'), 403
    
    # 404 – Page Not Found
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404
    
    # 404 – Method Not Allowed
    @app.errorhandler(405)
    def method_not_allowed(e):
        return render_template('405.html'), 405
    
    # 500 – Internal Server Error
    @app.errorhandler(500)
    def server_error(e):
        return render_template('500.html'), 500
    
def configure_logging(app):
    # Deactivate the default flask logger so that log messages do not get duplicated
    app.logger.removeHandler(default_handler)
    
    # Create a file handler object
    file_handler = RotatingFileHandler('flaskapp.log', maxBytes=16384, backupCount=20)
    
    # Set logging level of file handler object so it logs INFO & up
    file_handler.setLevel(logging.INFO)
    
    # Create file formatter object
    file_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(filename)s: %(lineno)d]')
    
    # Apply file formatter object to file handler
    file_handler.setFormatter(file_formatter)
    
    # Add file handler to logger
    app.logger.addHandler(file_handler)
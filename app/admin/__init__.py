from flask import Blueprint

admin_bp = Blueprint('admin', template_folder='templates')

from . import views
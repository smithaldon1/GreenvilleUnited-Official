from flask import Blueprint

partners_bp = Blueprint('partners', __name__, template_folder='templates')

from . import views
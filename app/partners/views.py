from . import partners_bp
from flask import render_template, request

@partners_bp.route('/')
def show_index():
    if request.method == 'GET':
        return render_template('partners/index.html')
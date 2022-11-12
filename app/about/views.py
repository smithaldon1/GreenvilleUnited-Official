from . import about_bp
from flask import render_template, request

@about_bp.route('/')
def show_index():
    if request.method == 'GET':
        return render_template('about/index.html')
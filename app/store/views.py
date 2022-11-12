from . import store_bp
from flask import render_template, request

@store_bp.route('/')
def show_index():
    if request.method == 'GET':
        return render_template('store/index.html')
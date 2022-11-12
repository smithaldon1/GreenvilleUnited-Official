from . import main_bp
from flask import render_template, request

@main_bp.route('/')
def show_index():
    success = False
    if request.method == 'POST':
        # TODO add new 
        if success:
            return render_template('main/thank-you.html')
        else:
            return render_template('404.html')
    if request.method == 'GET':
        return render_template('main/index.html')
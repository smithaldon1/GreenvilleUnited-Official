from . import main_bp
from flask import render_template, request

@main_bp.route('/')
def show_index():
    success = False
    if request.method == 'POST':
        # TODO add new 
        if success:
            title = 'Thank you!'
            return render_template('main/thank-you.html', title=title)
        else:
            title = 'Page Not Found...'
            return render_template('404.html', title=title)
    if request.method == 'GET':
        title = 'GUFC Goes National!'
        return render_template('main/index.html', title=title)
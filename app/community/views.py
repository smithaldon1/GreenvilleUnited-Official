from . import community_bp
from flask import render_template, request, abort

@community_bp.route('/')
def show_index():
    if request.method == 'GET':
        return render_template('community/index.html')
    else:
        return abort(404)
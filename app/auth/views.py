from . import auth_bp
from flask import render_template, request, url_for, redirect

@auth_bp.route('/')
def show_register():
    if request.method == 'GET':
        return render_template('auth/register.html')
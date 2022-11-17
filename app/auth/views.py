from . import auth_bp
from flask import render_template, request, url_for, redirect

@auth_bp.route('/')
def show_register():
    if request.method == 'GET':
        title = 'Register'
        # return render_template('auth/register.html', title=title)
        return render_template('under-construction.html', title=title)

@auth_bp.route('/')
def show_login(request):
    if request.method == 'GET':
        title = 'Login'
        # return render_template('auth/login.html', title=title)
        return render_template('under-construction.html', title=title)

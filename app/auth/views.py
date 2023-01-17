from . import auth_bp
from flask import render_template, request, url_for, redirect
from ..models import User
from app import db

try:
    email_table = db.session.scalars(db.select(User.email))
    userid_table = db.session.scalars(db.select(User.id))
except e as Exception:
    print(e)

@auth_bp.route('/register')
def show_register():
    if request.method == 'GET':
        return render_template('auth/register.html', title='Register')
        # return render_template('under-construction.html', title='Under Construction')
    elif request.method == 'POST':
        name = request.form.get(u'name')
        email = request.form.get(u'email')
        password = request.form.get(u'password')
        confPwd = request.form.get(u'confPass')
        
        if password == confPwd:
            user = User(email, password)
            db.session.add(user)
            db.session.commit()
        else:
            return None
            
@auth_bp.route('/login')
def show_login():
    if request.method == 'GET':
        return render_template('auth/login.html', title='Login')
        # return render_template('under-construction.html', title='Under Construction')
    elif request.method == 'POST':
        email = request.form.get(u'email')
        pwd = request.form.get(u'password')
        

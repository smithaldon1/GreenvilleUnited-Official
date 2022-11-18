from . import about_bp
from flask import render_template, request, redirect, url_for, make_response
from ..models import db, User
from datetime import datetime as dt


@about_bp.route('/')
def show_index():
    title = 'About'
    return render_template('about/index.html', title=title)

    
@about_bp.route('/league')
def show_league():
    title = 'About League'
    return render_template('about/league.html', title=title)

@about_bp.route('/vmc')
def show_vmc():
    title = 'Vision, Mission, Core'
    return render_template('about/vmc.html', title=title)

@about_bp.route('/team')
def show_team():
    title = 'About Team'
    return render_template('about/team.html', title=title)

@about_bp.route('/club')
def show_club():
    title = 'About Club'
    return render_template('about/club.html', title=title)

@about_bp.route('/players')
def show_players():
    title = 'About Players'
    return redirect(url_for('about.show_uc_page'))
    # return render_template('about/players.html', title=title)

@about_bp.route('/uc', methods=['GET', 'POST'])
def show_uc_page():
    if request.method == 'GET':
        title = 'Under Construction'
        return render_template('under-construction.html', title=title)
    
    if request.method == 'POST':
        email = request.form.get(u'email')
        if email:
            existing_user = User.query.filter(User.email == email).first()
            if existing_user:
                return make_response(f'{email} already subscribed!')
            new_user = User(email=email, created=dt.now())
            db.session.add(new_user) # adds new User record to database
            db.session.commit() # commits the change
        return make_response(f"{email} successfully subscribed!")
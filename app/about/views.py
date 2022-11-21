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
    # return redirect(url_for('about.show_uc_page'))
    return render_template('about/league.html', title=title)

@about_bp.route('/vmc')
def show_vmc():
    title = 'Vision, Mission, Core'
    # return redirect(url_for('about.show_uc_page'))
    return render_template('about/vmc.html', title=title)

@about_bp.route('/team')
def show_team():
    title = 'About Team'
    # return redirect(url_for('about.show_uc_page'))
    return render_template('about/team.html', title=title)

@about_bp.route('/club')
def show_club():
    title = 'About Club'
    # return redirect(url_for('about.show_uc_page'))
    return render_template('about/club.html', title=title)

@about_bp.route('/players')
def show_players():
    title = 'About Players'
    # return redirect(url_for('about.show_uc_page'))
    return render_template('about/players.html', title=title)

@about_bp.route('/uc', methods=['GET', 'POST'])
def show_uc_page():
    if request.method == 'GET':
        title = 'Under Construction'
        return render_template('under-construction.html', title=title)
    
    if request.method == 'POST':
        email = request.form.get(u'email')
        if email:
            title = "Thank You"
            existing_user = User.query.filter(User.email == email).first()
            if existing_user:
                htag = f"{email} is already subscribed!"
                ptag = "Thank you for supporting our club. The email you submitted is already subscribed to our newsletter."
                return render_template('main/thank-you.html', title=title, htag=htag, ptag=ptag)
            new_user = User(email=email, created=dt.now())
            db.session.add(new_user) # adds new User record to database
            db.session.commit() # commits the change
            htag = f"{email} successfully subscribed!"
            ptag = "Thank you for supporting our club. The email you submitted has been subscribed to our newsletter and you may unsubscribe at any time."
        return render_template('main/thank-you.html', title=title, htag=htag, ptag=ptag)
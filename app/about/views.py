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
    title = 'League'
    # return redirect(url_for('about.show_uc_page'))
    return render_template('about/league.html', title=title)

@about_bp.route('/vmc')
def show_vmc():
    title = 'Vision, Mission, Core'
    # return redirect(url_for('about.show_uc_page'))
    return render_template('about/vmc.html', title=title)

@about_bp.route('/team')
def show_team():
    title = 'Team'
    # return redirect(url_for('about.show_uc_page'))
    return render_template('about/team.html', title=title)

@about_bp.route('/club')
def show_club():
    title = 'Club'
    
    fernando = {'img_src': url_for('static', filename='img/fernando.png'), 'name': 'Fernando Zuniga', 'position': 'VP of Operations', 'description': "Mr. Zuniga enters his sixth season with the Chowan women's soccer team and fourth as head coach. During the 2020-21 season, Zuniga led the Hawks to one of their best seasons in program history sporting an 8-2-1 overall record and a 5-1-1 league record for second place in the league tables."}
    
    aaron = {'img_src': url_for('static', filename='img/aaron.png'), 'name': 'Fernando Zuniga', 'position': 'Director of Football', 'description': "Coach Okwei was born and raised in Osu, located in Accra, Ghana where he graduated from the Middlesbrough Soccer Academy before going on to play for the Desert Warriors who competed in the 2nd tier of Ghanaian football (soccer). Most recently, Okwei played for Greensboro International FC who compete in the UPSL"}
    
    luke = {'img_src': url_for('static', filename='img/luke.png'), 'name': 'Luke Staats', 'position': 'VP of Marketing', 'description': "Mr. Staats played four seasons of soccer at Lees-McRae (2008-12). He guided the team to three conference regular season and tournament titles, four straight NCAA Appearances, two trips to the NCAA Division II Sweet 16 and a national championship finalist appearance."}
    
    michael = {'img_src': url_for('static', filename='img/michael.png'), 'name': 'Michael McCarren', 'position': 'President', 'description': "Mr. McCarren is a business leader with 24 years of cross-functional experience in areas of business development, engineering, supply management, program management, marketing, and manufacturing. He holds 4 patents, 2 John Deere Presidents awards, 3 John Deere innovation awards, 1 Agritechnica innovation award, and 1 SPI Structure Design Award."}
    
    owners = [ fernando, aaron, luke, michael ]
    
    # return redirect(url_for('about.show_uc_page'))
    return render_template('about/club.html', title=title, owners=owners)

@about_bp.route('/players')
def show_players():
    title = 'Players'
    # return redirect(url_for('about.show_uc_page'))
    # return render_template('about/players.html', title=title)

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
from . import about_bp
from flask import render_template, request, redirect, url_for, make_response
from ..models import db, User, Staff, Player
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
    employees = []
    # return redirect(url_for('about.show_uc_page'))
    return render_template('about/team.html', title='Team', players=players, employees=employees)

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
    a_mbye = {'img_src': url_for('static', filename='img/Abdoulie-Mbye-greenville-united.png'), 'name': 'Abdoulie Mbye', 'position': 'Center Back', 'description': ''}
    a_ibuaka = {'img_src': url_for('static', filename='img/August-Ibuaka-greenville-united.png'), 'name': 'August Ibuaka', 'position': 'Center Back', 'description': ''}
    b_joseph = {'img_src': url_for('static', filename='img/Belony-Joseph-greenville-united.png'), 'name': 'Belony Joseph', 'position': 'Center Back', 'description': ''}
    b_martinez = {'img_src': url_for('static', filename='img/Bryan-Martinez-greenville-united.png'), 'name': 'Bryan Martinez', 'position': 'Center Back', 'description': ''}
    d_kaple = {'img_src': url_for('static', filename='img/Derek-Kaple-greenville-united.png'), 'name': 'Derek Kaple', 'position': 'Center Back', 'description': ''}
    e_corona = {'img_src': url_for('static', filename='img/Eriberto-Corona-greenville-united.png'), 'name': 'Eriberto Corona', 'position': 'Center Back', 'description': ''}
    g_saah = {'img_src': url_for('static', filename='img/Gabriel-Saah-greenville-united.png'), 'name': 'Gabriel Saah', 'position': 'Center Back', 'description': ''}
    i_pineda = {'img_src': url_for('static', filename='img/Ivan-Pineda-greenville-united.png'), 'name': 'Ivan Pineda', 'position': 'Center Back', 'description': ''}
    j_vaught = {'img_src': url_for('static', filename='img/jacob-vaught-greenville-united.png'), 'name': 'Jacob Vaught', 'position': 'Center Back', 'description': ''}
    j_makoko = {'img_src': url_for('static', filename='img/Jonathan-Makoko-greenville-united.png'), 'name': 'Jonathan Makoko', 'position': 'Center Back', 'description': ''}
    j_quiroga = {'img_src': url_for('static', filename='img/Jose-Quiroga-greenville-united.png'), 'name': 'Jose Quiroga', 'position': 'Center Back', 'description': ''}
    k_boafo = {'img_src': url_for('static', filename='img/Kenneth-Boafo-greenville-united.png'), 'name': 'Kenneth Boafo', 'position': 'Center Back', 'description': ''}
    k_boampong = {'img_src': url_for('static', filename='img/Kenneth-Boampong-greenville-united.png'), 'name': 'Kenneth Boampong', 'position': 'Center Back', 'description': ''}
    m_jallow = {'img_src': url_for('static', filename='img/Mamadou-Jallow-greenville-united.png'), 'name': 'Mamadou Jallow', 'position': 'Center Back', 'description': ''}
    m_raymond = {'img_src': url_for('static', filename='img/Marco-Dane-Raymond-greenville-united.png'), 'name': 'Marco Dane Raymond', 'position': 'Center Back', 'description': ''}
    m_ross = {'img_src': url_for('static', filename='img/Michael-Ross-greenville-united.png'), 'name': 'Michael Ross', 'position': 'Center Back', 'description': ''}
    m_fofana = {'img_src': url_for('static', filename='img/Muhamed-Fofana-greenville-united.png'), 'name': 'Muhamed Fofana', 'position': 'Center Back', 'description': ''}
    o_carlos = {'img_src': url_for('static', filename='img/Ochoa-Carlos-greenville-united.png'), 'name': 'Ochoa Carlos', 'position': 'Center Back', 'description': ''}
    o_espino = {'img_src': url_for('static', filename='img/Octavio-Espino-greenville-united.png'), 'name': 'Octavio Espino', 'position': 'Center Back', 'description': ''}
    q_murshed = {'img_src': url_for('static', filename='img/Qahtan-Murshed-greenville-united.png'), 'name': 'Qahtan Murshed', 'position': 'Center Back', 'description': ''}
    v_okafor = {'img_src': url_for('static', filename='img/valentine-okafor-greenville-united.png'), 'name': 'Valentine Okafor', 'position': 'Center Back', 'description': ''}
    v_hernandez = {'img_src': url_for('static', filename='img/victor-hernandez-greenville-united.png'), 'name': 'Victor Hernandez', 'position': 'Center Back', 'description': ''}
    
    players = [a_mbye, a_ibuaka, b_joseph, b_martinez, d_kaple, e_corona, g_saah, i_pineda, j_makoko, j_quiroga, j_vaught, k_boafo, k_boampong, m_fofana, m_jallow, m_raymond, m_ross, o_carlos, o_espino, q_murshed, v_hernandez, v_okafor]
    
    # return redirect(url_for('about.show_uc_page'))
    return render_template('about/players.html', title='Players', players=players)

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
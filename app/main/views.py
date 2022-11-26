from . import main_bp
from flask import render_template, request, url_for
from app import db


@main_bp.route('/')
def show_index():
    card1 = {
        'img_src': url_for('static', filename='img/season-standings-2022.png'),
        'img_title': '2022 Season Standings',
        'title': 'card.title', 
        'text': 'card.text'
    }
    card2 = {
        'img_src': url_for('static', filename='img/season-standings-2022.png'),
        'img_title': '2022 Season Standings',
        'title': 'card.title', 
        'text': 'card.text'
    }
    card3 = {
        'img_src': url_for('static', filename='img/season-standings-2022.png'),
        'img_title': '2022 Season Standings',
        'title': 'card.title', 
        'text': 'card.text'
    }
    spotlight_cards = [card1, card2, card3]
    title = 'GUFC Goes National!'
    return render_template('main/index.html', title=title, cards=spotlight_cards)

@main_bp.route('/donate')
def show_donate():
    return render_template('partners/donation.html', title='Make a Donation')

@main_bp.route('/site-map')
def show_site_map():
    title = 'Site Map'
    return render_template('main/site-map.html', title=title)

@main_bp.route('/privacy-policy')
def show_pp():
    return render_template('store/privacy-policy.html', title='Privacy Policy')
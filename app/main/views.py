from . import main_bp
from flask import render_template, request, url_for
from app import db


@main_bp.route('/')
def show_index():
    # Spotlight Initialization
    card1 = {
        'img_src': url_for('static', filename='img/season-standings-2022.png'),
        'img_title': '2022 Season Standings',
        'title': 'GUFC tops Coastal Standings!', 
        'text': 'Greenville United finishes the 2022 season at the top of the Coastal Standings. The team finished with 7 wins, 1 tie, and 2 losses, and a cumulative 21 points.'
    }
    card2 = {
        'img_src': url_for('static', filename='img/conference-final.png'),
        'img_title': 'Conference Final Image',
        'title': 'Conference Final Nov 19!', 
        'text': 'Check out our final game on November 19th!'
    }
    card3 = {
        'img_src': url_for('static', filename='img/gufc-vs-goldsboro.jpg'),
        'img_title': 'GUFC vs Goldsboro',
        'title': 'GUFC wins 3 - 0 against Goldsboro', 
        'text': 'Greenville United wins the season finale with a final score of 3 to nill. Fantastic work Bucks!'
    }
    spotlight_cards = [card1, card2, card3]
    
    # Sponsors Initialization
    carolina_vision = {
        'img_src': url_for('static', filename='img/carolina-vision-logo.png'),
        'name': 'Carolina Vision Care Logo',
    }
    
    partners = []
    sponsors = [carolina_vision]
    
    title = 'GUFC Goes National!'
    return render_template('main/index.html', title=title, cards=spotlight_cards, partners=partners, sponsors=sponsors)

@main_bp.route('/donate')
def show_donate():
    return render_template('partners/donation.html', title='Make a Donation')

@main_bp.route('/site-map')
def show_site_map():
    return render_template('main/site-map.html', title='Site Map')

@main_bp.route('/privacy-policy')
def show_pp():
    return render_template('store/privacy-policy.html', title='Privacy Policy')
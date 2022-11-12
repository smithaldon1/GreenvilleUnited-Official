from . import about_bp
from flask import render_template, request

@about_bp.route('/')
def show_index():
    if request.method == 'GET':
        title = 'About'
        return render_template('about/index.html', title=title)
    
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
    return render_template('about/players.html', title=title)

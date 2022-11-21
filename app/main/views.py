from . import main_bp
from flask import render_template, request
from app import db


@main_bp.route('/')
def show_index():
    
    title = 'GUFC Goes National!'
    return render_template('main/index.html', title=title)

@main_bp.route('/donate')
def show_donate():
    return render_template('partners/donation.html', title='Make a Donation')

@main_bp.route('/site-map')
def show_site_map():
    title = 'Site Map'
    return render_template('main/site-map.html', title=title)
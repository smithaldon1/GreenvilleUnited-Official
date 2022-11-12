from . import partners_bp
from flask import render_template, request

@partners_bp.route('/')
def show_index():
    if request.method == 'GET':
        title = 'Partners'
        return render_template('partners/index.html', title=title)
    
@partners_bp.route('/local-sponsors')
def show_local_sponsors():
    title = 'Local Sponsors'
    return render_template('partners/local-sponsors.html', title=title)

@partners_bp.route('/partner')
def show_partner():
    title = 'Become A Partner'
    return render_template('partners/partner.html', title=title)

@partners_bp.route('/donation')
def show_donation():
    title = 'Make A Donation'
    return render_template('partners/donation.html', title=title)
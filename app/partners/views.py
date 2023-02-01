from . import partners_bp
from flask import render_template, request

@partners_bp.route('/partners')
def show_index():
    title = 'Partners'
    # return render_template('partners/index.html', title=title)
    return render_template('under-construction.html', title=title)
    
@partners_bp.route('/sponsors')
def show_sponsors():
    title = 'Sponsors'
    # return render_template('partners/sponsors.html', title=title)
    return render_template('under-construction.html', title=title)
    

@partners_bp.route('/donation-policy')
def show_donation_pp():
    title = 'Donation Policy'
    return render_template('partners/donation-policy.html', title=title)
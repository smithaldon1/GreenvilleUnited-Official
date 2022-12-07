from . import store_bp
from flask import render_template, request

@store_bp.route('/')
def show_index():
    if request.method == 'GET':
        title = 'Store'
        return render_template('under-construction.html', title=title) 
        # return render_template('store/index.html', title=title)
    
@store_bp.route('/tickets')
def show_tickets():
    title = 'Purchase Tickets'
    # return render_template('store/tickets.html', title=title)
    return render_template('under-construction.html', title=title)

@store_bp.route('/team')
def show_team_store():
    title = 'Team Store'
    # return render_template('store/team-store.html', title=title)
    return render_template('under-construction.html', title=title)

@store_bp.route('/support')
def show_support():
    title = 'Support'
    # return render_template('store/support.html', title=title)
    return render_template('under-construction.html', title=title)

@store_bp.route('/terms-conditions')
def show_terms():
    title = 'Terms and Conditions'
    # return render_template('store/terms-conditions.html', title=title)
    return render_template('under-construction.html', title=title)

@store_bp.route('/privacy-policy')
def show_pp():
    title = 'Privacy Policy'
    # return render_template('store/privacy-policy.html', title=title)
    return render_template('under-construction.html', title=title)
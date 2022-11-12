from . import store_bp
from flask import render_template, request

@store_bp.route('/')
def show_index():
    if request.method == 'GET':
        return render_template('store/index.html', title=title)
    
@store_bp.route('/tickets')
def show_tickets():
    title = 'Purchase Tickets'
    return render_template('store/tickets.html', title=title)

@store_bp.route('/team')
def show_team_store():
    title = 'Team Store'
    return render_template('store/team-store.html', title=title)

@store_bp.route('/support')
def show_support():
    title = 'Support'
    return render_template('store/support.html', title=title)
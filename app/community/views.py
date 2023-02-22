from . import community_bp
from flask import render_template, request, abort
from app import db

@community_bp.route('/')
def show_index():
    if request.method == 'GET':
        title = 'Community'
        # return render_template('community/index.html', title=title)
        return render_template('under-construction.html', title=title)
    else:
        return abort(404)
    
@community_bp.route('/youth')
def show_youth():
    title = 'Youth'
    return render_template('community/youth.html', title=title)
    # return render_template('under-construction.html', title=title)

@community_bp.route('/engagement')
def show_engagement():
    title = 'Community Engagement'
    # return render_template('community/engagement.html', title=title)
    return render_template('under-construction.html', title=title)

@community_bp.route('/schedule')
def show_schedule():
    title = 'Schedule'
    events = {}
    # return render_template('community/2023.html', title=title, events=events)
    return render_template('under-construction.html', title=title)

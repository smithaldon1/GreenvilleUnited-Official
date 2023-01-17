from . import admin_bp
from flask import render_template, request, redirect
from app import db
from app.models import Donation, Event

@admin_bp.route('/donations')
def show_index():
    if request.method == 'GET':
        stmt = db.select(Donation).where(Donation.amount >= 1.00)
        donations = db.session.scalars(stmt)
        return render_template('admin/index.html', title='Admin Portal', donations=donations)
    elif request.method == 'POST':
        return None
    # if user:
    #     return render_template('admin/index.html', title="Admin Dashboard")
    # else:
    #     return None
    
@admin_bp.route('/events', methods=['GET', 'POST'])
def show_events():
    if request.method == 'GET':
        events = {}
        return render_template('admin/events.html', title='Events Admin', events=events)
    elif request.method == 'POST':
        # Assign form values
        title = request.form['title']
        descript = request.form['descript']
        start_time = request.form['startTime']
        end_time = request.form['endTime']
        cost = request.form['cost']
        physical_addr = request.form['address']
        
        # Create event object
        event = Event(start_time, end_time, title, descript, cost, physical_addr)
        
        # Add event and commit to db
        db.session.add(event)
        db.session.commit()
        return event
        
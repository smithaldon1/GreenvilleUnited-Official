from . import admin_bp
from flask import render_template, request
from app import db
from app.models import Donation

@admin_bp.route('/')
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
    

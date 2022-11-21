from . import admin_bp
from flask import render_template, request
from app import db

@admin_bp.route('/')
def show_index():
    if user:
        return render_template('admin/index.html', title="Admin Dashboard")
    else:
        return None
    

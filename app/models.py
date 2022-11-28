from . import db
from sqlalchemy import Enum

class User(db.Model):
    """Data model for newsletter users"""
    __tablename__ = 'gufc-newsletter-users'
    id = db.Column(db.Integer, primary_key=True )
    email = db.Column(db.String(255), index=False,unique=True, nullable=False)
    created = db.Column(db.DateTime, index=False, unique=False, nullable=False)
    
    def __repr__(self):
        return '<User {}>'.format(self.email)

class Player(db.Model):
    __tablename__ = 'gufc-team-roster'
    id = db.Column(db.Integer, primary_key=True)
    img_src = db.Column(db.String, nullable=False)
    name = db.Column(db.String(255), nullable=False, unique=True)
    position = db.Column(db.String(3), unique=False, nullable=False)
    description = db.Column(db.String, nullable=False)
    
    def __repr__(self):
        return f"Player(id='{self.id}', img_src='{self.img_src}', name='{self.name}', pos='{self.position}, desc='{self.description}')"
    
class Staff(db.Model):
    __tablename__ = 'gufc-staff-roster'
    id = db.Column(db.Integer, primary_key=True)
    img_src = db.Column(db.String, nullable=False)
    name = db.Column(db.String(255), nullable=False, unique=True)
    position = db.Column(db.String(3), unique=False, nullable=False)
    description = db.Column(db.String, nullable=False)
    
    def __repr__(self):
        return f"Staff(id='{self.id}', img_src='{self.img_src}', name='{self.name}', pos='{self.position}, desc='{self.description}')"
    
class Card(db.Model):
    __tablename__ = 'gufc-cards'
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, index=False, unique=False, nullable=False)
    author = db.Column(db.String(255), index=False, unique=False, nullable=False)
    img_src = db.Column(db.String, nullable=False)
    img_title = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    body_text = db.Column(db.String, nullable=False)
    link_url = db.Column(db.String, nullable=False)
    link_text = db.Column(db.String, nullable=False)
    
    def __repr__(self):
        return '<Card {}>'.format(self.id)
    
class Match(db.Model):
    __tablename__ = 'gufc-matches'
    id = db.Column(db.Integer, primary_key=True)
    match_date = db.Column(db.DateTime, index=True, unique=True, nullable=False)
    opponent = db.Column(db.String, index=True, unique=False, nullable=False)
    logo_src = db.Column(db.String, index=False, unique=False, nullable=False)
    
    def __repr__(self):
        return '<Match {}>'.format(self.match_date)
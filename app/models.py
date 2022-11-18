from . import db

class User(db.Model):
    """Data model for newsletter users"""
    
    __tablename__ = 'gufc-newsletter-users'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    email = db.Column(
        db.String(255),
        index=False,
        unique=True,
        nullable=False
    )
    created = db.Column(
        db.DateTime,
        index=False,
        unique=False,
        nullable=False
    )
    
    def __repr__(self):
        return '<User {}>'.format(self.email)
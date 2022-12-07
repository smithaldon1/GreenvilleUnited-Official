from . import db
# from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Float
# from sqlalchemy.orm import declarative_base, relationship

# declarative base class
# Base = declarative_base()

# User Model
class User(db.Model):
    """Data model for website users"""
    __tablename__ = 'gufc-users'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    email = db.Column(db.String(255), index=False, unique=True, nullable=False)
    created = db.Column(db.DateTime, index=False, unique=False, nullable=False)
    
    def __repr__(self):
        return f"User(id={self.id!r}, email={self.email}, created={self.created})"


# Donation Model
class Donation(db.Model):
    __tablename__ = 'gufc-donations'
    id = db.Column(db.Integer, primary_key=True)
    d_created = db.Column(db.DateTime, index=False, unique=False, nullable=False)
    amount = db.Column(db.Float, unique=False, nullable=False)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.NVARCHAR(10), nullable=True)
    zip_code = db.Column(db.NVARCHAR(5), nullable=False)
    
    def __repr__(self):
        return f"Donation(id={self.id}, donation_created={self.d_created}, amount={self.amount}, donation_user='{self.first_name} {self.last_name}', email={self.email}, phone={self.phone}, zip_code={self.zip_code})"


# Player Model
class TeamMember(db.Model):
    __tablename__ = 'gufc-team'
    id = db.Column(db.Integer, primary_key=True)
    img_src = db.Column(db.String, nullable=False)
    name = db.Column(db.String(255), nullable=False, unique=True)
    position = db.Column(db.String(3), unique=False, nullable=False)
    description = db.Column(db.String, nullable=False)
    
    def __repr__(self):
        return f"TeamMember(id={self.id}, img_src={self.img_src}, name={self.name}, pos={self.position}, desc={self.description})"
    

# Card Model
class Article(db.Model):
    __tablename__ = 'gufc-news'
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, index=False, unique=False, nullable=False)
    # author = ForeignKey(TeamMember.name, default='GUFC Admin')
    img_src = db.Column(db.String, nullable=False)
    img_title = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    body_text = db.Column(db.String, nullable=False)
    link_url = db.Column(db.String, nullable=False)
    link_text = db.Column(db.String, nullable=False)
    
    def __repr__(self):
        return f"Article(id={self.id}, created={self.created}, author={self.author}, img_src={self.img_src}, img_title={self.img_title}, title={self.title}, body_text={self.body_text}, link_url={self.link_url}, link_text={self.link_text})"
    

# Match Model
class Match(db.Model):
    __tablename__ = 'gufc-matches'
    id = db.Column(db.Integer, primary_key=True)
    match_date = db.Column(db.DateTime, index=True, unique=True, nullable=False)
    opponent = db.Column(db.String, index=True, unique=False, nullable=False)
    logo_src = db.Column(db.String, index=False, unique=False, nullable=False)
    
    def __repr__(self):
        return f"Match(id={self.id}, match_date={self.match_date}, opponent={self.opponent}, logo_src={self.logo_src})"
    
class Main(db.Model):
    __tablename__ = 'gufcMain'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    value = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f"Main(id={self.id}, name={self.name}, value={self.value})"
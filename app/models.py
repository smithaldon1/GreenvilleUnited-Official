from . import db
from datetime import datetime as dt

# User Model
class User(db.Model):
    """Data model for website users"""
    __tablename__ = 'gufcusers'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    email = db.Column(db.String(255), index=False, unique=True, nullable=False)
    password = db.Column(db.String(255), index=False, unique=False, nullable=False)
    created = db.Column(db.DateTime, index=False, unique=False, nullable=False)
    
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.created = dt.now()
    
    def __repr__(self):
        return f"User(id={self.id!r}, email={self.email}, password={self.password}, created={self.created})"


# Donation Model
class Donation(db.Model):
    """ 
    Data model 
    """
    __tablename__ = 'gufcdonations'
    id = db.Column(db.Integer, primary_key=True)
    d_created = db.Column(db.DateTime, index=False, unique=False, nullable=False)
    amount = db.Column(db.Integer, unique=False, nullable=False)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(13), nullable=True)
    zip_code = db.Column(db.String(5), nullable=False)
    
    def __init__(self, amount, first_name, last_name, email, phone, zip_code):
        self.d_created = dt.now()
        self.amount = amount
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.zip_code = zip_code
    
    def __repr__(self):
        return f"Donation(id={self.id}, donation_created={self.d_created}, amount={self.amount}, donation_user='{self.first_name} {self.last_name}', email={self.email}, phone={self.phone}, zip_code={self.zip_code})"


# Player Model
class TeamMember(db.Model):
    __tablename__ = 'gufcTeam'
    id = db.Column(db.Integer, primary_key=True)
    img_src = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False, unique=True)
    position = db.Column(db.String(3), unique=False, nullable=False)
    description = db.Column(db.String(255), nullable=True)
    
    def __init__(self, img_src, name, position, description):
        self.img_src = img_src
        self.name = name
        self.position = position
        self.description = description
    
    def __repr__(self):
        return f"TeamMember(id={self.id}, img_src={self.img_src}, name={self.name}, pos={self.position}, desc={self.description})"
    

# Card Model
class Article(db.Model):
    __tablename__ = 'gufcNews'
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, index=False, unique=False, nullable=False)
    # author = ForeignKey(TeamMember.name, default='GUFC Admin')
    img_src = db.Column(db.String(255), nullable=False)
    img_title = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    body_text = db.Column(db.String(5000), nullable=False)
    link_url = db.Column(db.String(255), nullable=False)
    link_text = db.Column(db.String(255), nullable=False)
    
    def __init__(self, img_src, img_title, title, body_text, link_url, link_text):
        self.created = dt.now()
        self.img_src = img_src
        self.img_title = img_title
        self.title = title
        self.body_text = body_text
        self.link_url = link_url
        self.link_text = link_text
    
    def __repr__(self):
        return f"Article(id={self.id}, created={self.created}, author={self.author}, img_src={self.img_src}, img_title={self.img_title}, title={self.title}, body_text={self.body_text}, link_url={self.link_url}, link_text={self.link_text})"
    

# Match Model
class Match(db.Model):
    __tablename__ = 'gufcMatches'
    id = db.Column(db.Integer, primary_key=True)
    match_date = db.Column(db.DateTime, index=True, unique=True, nullable=False)
    opponent = db.Column(db.String(255), index=True, unique=False, nullable=False)
    logo_src = db.Column(db.String(255), index=False, unique=False, nullable=False)
    
    def __init__(self, match_date, opponent, logo_src):
        self.match_date = match_date
        self.opponent = opponent
        self.logo_src = logo_src
    
    def __repr__(self):
        return f"Match(id={self.id}, match_date={self.match_date}, opponent={self.opponent}, logo_src={self.logo_src})"
    
class Main(db.Model):
    __tablename__ = 'gufcmain'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    value = db.Column(db.Integer, nullable=False)
    
    def __init__(self, name, value):
        self.name = name
        self.value = value
    
    def __repr__(self):
        return f"Main(id={self.id}, name={self.name}, value={self.value})"
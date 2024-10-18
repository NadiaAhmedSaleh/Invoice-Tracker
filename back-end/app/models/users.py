from app.extensions import db
from flask_login import UserMixin 
from werkzeug.security import generate_password_hash, check_password_hash 
from app import login_manager
from flask import render_template, url_for, request, redirect



class Users(db.Model, UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(100), nullable=False)
    full_name=db.Column(db.String(100), nullable=False)
    email=db.Column(db.String(100), unique=True, nullable=False)
    password=db.Column(db.String(128), nullable=False)

    def __init__(self, username, password, email, full_name):
        self.username=username
        self.password=password
        self.email=email
        self.full_name=full_name



    @property
    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'full_name': self.full_name,
            'email': self.email
        }
    
    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def set_password(self, password):
        self.password = generate_password_hash(password)

    
@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)  
             

from datetime import datetime
from app.extensions import db

class Users(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    user_name=db.Column(db.String(100), nullable=False)
    full_name=db.Column(db.String(100), nullable=False)
    email=db.Column(db.String(100), nullable=False)
    password=db.Column(db.String(100), nullable=False)

    
    @property
    def serialize(self):
        return {
            'id': self.id,
            'user_name': self.user_name,
            'full_name': self.full_name,
            'email': self.email
        }
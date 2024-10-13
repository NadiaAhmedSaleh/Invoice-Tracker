from app.extensions import db
from app.models.users import Users

class Invoice(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    issuer=db.Column(db.String(100), nullable=False)
    status=db.Column(db.String(100), nullable=False)
    amount=db.Column(db.Integer, nullable=False)
    date_issued=db.Column(db.Date, nullable=False)
    due_date=db.Column(db.Date, nullable=False)
    user_id=db.Column(db.Integer, db.ForeignKey(Users.id))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'issuer': self.issuer,
            'status': self.status,
            'amount': self.amount,
            'date_issued': self.date_issued,
            'due_date': self.due_date,
            'user_id': self.user_id
        }
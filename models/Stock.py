from db import db

class Stock(db.Model):
    __tablename__ = 'stocks'

    id = db.Column(db.Integer, primary_key=True)
    Type = db.Column(db.String(45))
    product = db.Column(db.String(45))
    Amount = db.Column(db.Integer)
    Date = db.Column(db.String(45))
    

    def __init__(self, *args, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)

    def json(self):
        return {
            'id': self.id,
            'Type': self.Type,
            'product': self.product,
            'Amount': self.Amount,
            'Date': self.Date
        }


    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
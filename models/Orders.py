from db import db

class Orders(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    orderid  = db.Column(db.String(45))
    totalbill = db.Column(db.String(45))
    customername = db.Column(db.String(45))
    recordedby = db.Column(db.String(45))
    customerid = db.Column(db.String(45))
    date  = db.Column(db.String(45))

    def __init__(self, *args, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)
                
    def json(self):
        return {
            'id': self.id,
            'totalbill': self.totalbill,
            'recordedby': self.recordedby,
            'data':self.date,
            'customerid': self.customerid,
            'customername': self.customername,
        }
    
    @staticmethod
    def getById(_id):
        return Orders.query.filter_by(id=_id).first()

    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()


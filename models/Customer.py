from db import db

class Customer(db.Model):
    __tablename__ = 'customers'

    Customerid = db.Column(db.Integer, primary_key=True)
    CustomerName = db.Column(db.String(45))
    CustomerAddress = db.Column(db.String(45))
    CustomerNumber = db.Column(db.String(45))
    ContainersOnHand = db.Column(db.Integer())

    def __init__(self, *args, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)

    def json(self):
        return {
            'id':self.Customerid,
            'name': self.CustomerName,
            'address': self.CustomerAddress,
            'number': self.CustomerNumber,
            'onhand': self.ContainersOnHand
        }

    @classmethod
    def getById(cls, _id):
        return cls.query.filter_by(Customerid=_id).first()


    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
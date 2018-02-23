from db import db
from sqlalchemy import update
from flask_sqlalchemy import SQLAlchemy

class Orders(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    orderid  = db.Column(db.String(45))
    totalbill = db.Column(db.String(45))
    customername = db.Column(db.String(45))
    recordedby = db.Column(db.String(45))
    customerid = db.Column(db.String(45))
    status = db.Column(db.String(45))
    date  = db.Column(db.String(45))

    def __init__(self, *args, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)
                
    def json(self):
        return {
            'id': self.id,
            'totalbill': self.totalbill,
            'orderid': self.orderid,
            'recordedby': self.recordedby,
            'date':self.date,
            'customerid': self.customerid,
            'customername': self.customername,
            'status': self.status,
        }
    
    @staticmethod
    def getById(_id):
        return Orders.query.filter_by(orderid=_id).first()


    def getByCustomerId(_customerid):
        return Orders.query.filter_by(customerid=_customerid).all()
   
    def insert(self):
        db.session.add(self)
        db.session.commit()
        
    def commit(self):
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    


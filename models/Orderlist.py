from db import db

class Orderlist(db.Model):
    __tablename__ = 'orderlist'

    id = db.Column(db.Integer, primary_key=True)
    orderid  = db.Column(db.String(45))
    productid = db.Column(db.String(45))
    pname = db.Column(db.String(45))
    quantity = db.Column(db.String(45))
    subtotal = db.Column(db.String(45))
    totalbill =db.Column(db.String(45))

    def __init__(self, *args, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)
                
    def test():
        return {}

    def json(self):
        return {
            'id': self.id,
            'orderid': self.orderid,
            'pname': self.pname,
            'productid': self.productid,
            'quantity': self.quantity,
            'subtotal': self.subtotal,
            'totalbill': self.totalbill,
        }
    
    @staticmethod
    def getById(_id):   
        return Orderlist.query.filter_by(orderid=_id).all()

    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()


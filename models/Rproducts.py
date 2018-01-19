from db import db

class Rproducts(db.Model):
    __tablename__ = 'rentalproducts'

    

    id = db.Column(db.Integer, primary_key=True)
    rproductname  = db.Column(db.String(45))
    rprice = db.Column(db.String(30))
    rquantity = db.Column(db.String(20))


    def __init__(self, *args, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)
                
    def json(self):
        return {
            'id': self.id,
            'rproductname': self.rproductname,
            'rprice': self.rprice,
            'rquantity': self.rquantity,
        }


    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()


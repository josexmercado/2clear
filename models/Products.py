from db import db

class products(db.Model):
    __tablename__ = 'products'

    

    id = db.Column(db.Integer, primary_key=True)
    pname  = db.Column(db.String(45))
    pprice = db.Column(db.String(45))
    quantity = db.Column(db.String(45))


    def __init__(self, *args, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)
                
    def json(self):
       return {'id':self.id}

    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()


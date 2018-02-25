from db import db
from sqlalchemy import update
from flask_sqlalchemy import SQLAlchemy


class CustomerModel(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    number = db.Column(db.String(45))
    address = db.Column(db.String(45))
    onhandid = db.Column(db.String(45))
    topay = db.Column(db.String(45))
    account = db.Column(db.String(45))

    def __init__(self, *args, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)

    def json(self):
        return {
            'id':self.id,
            'name': self.name,
            'address': self.address,
            'onhandid':self.onhandid,
            'number': self.number,
            'topay': self.topay,
            'account': self.account,
        }

    @staticmethod
    def getById(_id):
        return CustomerModel.query.filter_by(id=_id).first()

    def getByName(_name):
        return CustomerModel.query.filter_by(name=_name).first()

    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
            
    def commit(self):
        db.session.commit()
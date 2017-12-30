from db import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(45))
    password = db.Column(db.String(45))
    role = db.Column(db.String(45))
    name = db.Column(db.String(45))

    def __init__(self, *args, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)

    def insert(self):
        db.session.add()
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
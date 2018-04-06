from db import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import update

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

    def json(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'role': self.role,
            'name': self.name
        }

    @staticmethod
    def getUserId(_id):
        return User.query.filter_by(id=_id).first()
    
    def find_by_username(_username):
        return User.query.filter_by(username=_username).first()

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def commit(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
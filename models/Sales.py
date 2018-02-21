from db import db

class Sales(db.Model):
    __tablename__ = 'sales'

    salesid = db.Column(db.Integer, primary_key=True)
    customerid = db.Column(db.String(45))
    customername = db.Column(db.String(45))
    totalsale = db.Column(db.Integer)
    recordedby = db.Column(db.String(45))
    date = db.Column(db.String(50))
    ordernumber = db.Column(db.String(50))

    def __init__(self, *args, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)

    def json(self):
        return {
            'salesid': self.salesid,
            'ordernumber':self.ordernumber,
            'customerid': self.customerid,
            'customername': self.salesid,
            'totalsale': self.totalsale,
            'recordedby': self.recordedby,
            'date': self.date
        }

    @staticmethod
    def getBydate(_date):
        return Sales.query.filter_by(date=_date).first()

    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

        
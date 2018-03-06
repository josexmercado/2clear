from flask_restful import Resource, reqparse
from models.Stock import Stock
from datetime import datetime

class UpdateStocks(Resource):
	def get(self):
		print("FUN") 
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('type',
			type=str,
			required=True,
			help="This field cannot be left blank!"
			)
		parser.add_argument('product',
			type=str,
			required=True,
			help="This field cannot be left blank!"
			)
		parser.add_argument('amount',
			type=str,
			required=True,
			help="This field cannot be left blank!"
			)
		parser.add_argument('date',
			type=str,
			required=True,
			help="This field cannot be left blank!"
			)
		parser.add_argument('recby',
			type=str,
			required=True,
			help="This field cannot be left blank!"
			)
		parser.add_argument('mm',
			type=str,
			required=True,
			help="This field cannot be left blank!"
			)
		data = parser.parse_args()

		new_stocks = Stock(
			product=data.product,
			amount=data.amount,
			type=data.type,
			date=data.date,
			recby=data.recby,
			mm=data.mm
			)

		new_stocks.insert()
		return {'message':'Stocks Updated!','button id="confirm"':'OK'}
class getBymonth(Resource):
	def get(self, _mm):
	
		stocklist = Stock.getBymonth(_mm)
		
		return [stock.json() for stock in stocklist]


class getByweek(Resource):
	def get(self, _week):
	
		week = Stock.getByweek(_week)
		datetime.strptime(week, '%m-%d-%y')
		
		return [stock.json() for stock in stocklist]

class getBydate(Resource):
	def get(self, _date):
	
		stocklist = Stock.getBydate(_date)
		
		return [stock.json() for stock in stocklist]

class getBydatexx(Resource):
	def get(self, _date):
	
		stocklist = Stock.getBydate(_date)
		startdate = datetime.timedelta(stocklist.date)
		enddate = Stock.getBydate(_date)
		return [stock.json() for stock in stocklist]


class getBydatex(Resource):
	def get(self, _date):
	
		stocklist = Stock.getBydatex(_date)
		
		return [stock.json() for stock in stocklist]
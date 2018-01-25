from flask_restful import Resource, reqparse
from models.Stock import Stock

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
		data = parser.parse_args()

		new_stocks = Stock(
			product=data.product,
			amount=data.amount,
			type=data.type,
			date=data.date
			)

		new_stocks.insert()
		return {'message':'Stocks Updated!'}
from flask_restful import Resource, reqparse
from models.Stock import Stock

class updatestocks(Resource):

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
		data = parser.parse_args()

		new_stocks = Stock(
			product=data.product,
			amount=data.amount,
			)
		new_stocks.insert()
		return {'message':'Stocks Updated!'}
from flask_restful import Resource, reqparse
from models.Orders import Orders
from models.Orderlist import Orderlist
from models.Sales import Sales

class recordsales(Resource):

	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('ordernumber',
			type=str,
			# required=True,
			help="This field cannot be left blank!"
			)
		parser.add_argument('customerid',
			type=str,
			# required=True,
			help="This field cannot be left blank!"
			)
		parser.add_argument('customername',
			type=str,
			# required=True,
			help="This field cannot be left blank!"
			)
		parser.add_argument('totalsale',
			type=str,
			# required=True,
			help="This field cannot be left blank!"
			)
		parser.add_argument('recordedby',
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

		new_sales = Sales(
			customerid=data.customerid,
			ordernumber=data.ordernumber,
			customername=data.customername,
			totalsale=data.totalsale,
			recordedby=data.recordedby,
			date=data.date,
			)
		new_sales.insert()
		return {'message':'New SAles!'}

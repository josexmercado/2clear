from flask_restful import Resource, reqparse
from models.Orders import Orders
from models.Orderlist import Orderlist
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import update
from db import db

class registerorder(Resource):

	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('orderid',
			type=str,
			required=True,
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
		parser.add_argument('totalbill',
			type=str,
			# required=True,
			help="This field cannot be left blank!"
			)
		parser.add_argument('recordedby',
			type=str,
			# required=True,
			help="This field cannot be left blank!"
			)
		parser.add_argument('date',
			type=str,
			# required=True,
			help="This field cannot be left blank!"
			)
		parser.add_argument('status',
			type=str,
			# required=True,
			help="This field cannot be left blank!"
			)
		data = parser.parse_args()

		new_orders = Orders(
			orderid=data.orderid,
			customerid=data.customerid,
			customername=data.customername,
			totalbill=data.totalbill,
			recordedby=data.recordedby,
			date=data.date,
			status=data.status
			)
		new_orders.insert()
		return {'message':'New Order Registered!'}

class recordorderlist(Resource):

	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('orderid',
			type=str,
			#required=True,
			help="This field cannot be left blank!"
			)
		parser.add_argument('productid',
			type=str,
			# required=True,
			help="This field cannot be left blank!"
			)
		parser.add_argument('pname',
			type=str,
			# required=True,
			help="This field cannot be left blank!"
			)
		parser.add_argument('quantity',
			type=str,
			# required=True,
			help="This field cannot be left blank!"
			)
		parser.add_argument('subtotal',
			type=str,
			# required=True,
			help="This field cannot be left blank!"
			)
		data = parser.parse_args()

		new_orderlist = Orderlist(
			orderid=data.orderid,
			productid=data.productid,
			pname=data.pname,
			quantity=data.quantity,
			subtotal=data.subtotal
			)
		new_orderlist.insert()
		return {'message':'Orderlist Recorded!'}

class salescustomer(Resource):

	def get(self, _id):
	
		customer = Orders.getById(_id)

		return customer.json()

class orderid(Resource):

	def get(self, _orderid):
	
		ordernumber = Orders.getById(_orderid)

		return ordernumber.json()

class approveorder(Resource):

	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('orderid',
			type=str,
			required=True,
			help="This field cannot be left blank!"
			)
		parser.add_argument('status',
			type=str,
			required=True,
			help="This field cannot be left blank!"
			)
		data = parser.parse_args()
		Orderss = Orders.getById(data.orderid)
		updatex = Orders.query.filter_by(orderid=Orderss.orderid).first()
		updatex.status= "delivered"
		updatex.commit()

		return {'message':'Order Approved!'}
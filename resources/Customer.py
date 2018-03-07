from flask_restful import Resource, reqparse
from models.CustomerModel import CustomerModel
from models.Orderlist import Orderlist
from models.Orders import Orders
from models.Products import Products
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import update
from db import db


class CustomerRegister(Resource):

	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('customername',
			type=str,
			required=True,
			help="This field cannot be left blank!"
			)
		parser.add_argument('customeraddress',
			type=str,
			required=True,
			help="This field cannot be left blank!"
			)
		parser.add_argument('customercontact',
			type=str,
			required=True,
			help="This field cannot be left blank!"
			)
		parser.add_argument('onhandid',
			type=str,
			required=True,
			)
		parser.add_argument('topay',
			type=str,
			required=True,
			)
		parser.add_argument('account',
			type=str,
			required=True,
			)
		data = parser.parse_args()

		new_customer = CustomerModel(
			name=data.customername,
			address=data.customeraddress,
			number=data.customercontact,
			onhandid=data.onhandid,
			topay=data.topay,
			account=data.account
			)
		new_customer.insert()
		return {'message':'Customer added!'}
class getcustomer(Resource):

	def get(self, _name):
	
		customername= CustomerModel.getByName(_name)

		return customername.json()

class UpdateAccount(Resource):
	
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('id',
			type=str,
			)
		parser.add_argument('account',
			type=int,
			required=True,
			help="This field cannot be left blank!"
			)
		data = parser.parse_args()
		customer = CustomerModel.getById(data.id)
		updatex = CustomerModel.query.filter_by(id=customer.id).first()
		updatex.account= updatex.account - data.account
		updatex.commit()

		return {'message':'Customer Updated!'}


class UpdateAccount2(Resource):
	
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('id',
			type=str,
			)
		parser.add_argument('account',
			type=int,
			required=True,
			help="This field cannot be left blank!"
			)
		data = parser.parse_args()
		customer = CustomerModel.getById(data.id)
		updatex = CustomerModel.query.filter_by(id=customer.id).first()
		updatex.account= updatex.account + data.account
		updatex.commit()

		return {'message':'Customer Updated!'}


class UpdateCustomer(Resource):
	
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('name',
			type=str,
			)
		parser.add_argument('address',
			type=str,
			required=True,
			help="This field cannot be left blank!"
			)
		parser.add_argument('number',
			type=str,
			required=True,
			help="This field cannot be left blank!"
			)
		data = parser.parse_args()
		customer = CustomerModel.getByName(data.name)
		updatex = CustomerModel.query.filter_by(name=customer.name).first()
		updatex.name= data.name
		updatex.address= data.address
		updatex.number= data.number
		updatex.commit()

		return {'message':'Customer Updated!'}

class deletecustomer(Resource):

	def delete(self):
		parser = reqparse.RequestParser()
		parser.add_argument('name',
			type=str,
			)
		data = parser.parse_args()
		customer = CustomerModel.getByName(data.name)
		delname = CustomerModel.query.filter_by(name = customer.name).first()
		delname.delete()
		delname.commit()
		return {'message':'Product deleted!'}
		
class CustomerData(Resource):

	def get(self, _id):
	
		customer = CustomerModel.getById(_id)

		return customer.json()


class customercontainer(Resource):
	
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('orderid',
			type=str,
			required=True,
			help="This field cannot be left blank!"
			)
		parser.add_argument('type',
			type=str,
			required=True,
			help="This field cannot be left blank!"
			)
		parser.add_argument('quantity',
			type=int,
			# required=True,
			help="This field cannot be left blank!"
			)
		data = parser.parse_args()
		Orderss = Orders.getById(data.orderid)
		xupdatex = CustomerModel.query.filter_by(id=Orderss.customerid).first()
		xupdatex.onhandid = CustomerModel.onhandid + data.quantity

		xupdatex.commit()

		return {'message':'wow!'}


class returncontainer(Resource):
	
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('id',
			type=int,
			# required=True,
			help="This field cannot be left blank!"
			)
		parser.add_argument('quantity',
			type=int,
			# required=True,
			help="This field cannot be left blank!"
			)
		data = parser.parse_args()
		xupdatex = CustomerModel.query.filter_by(id=data.id).first()
		xupdatex.onhandid = CustomerModel.onhandid - data.quantity
		xupdatex.commit()

		xupdatep = Products.query.filter_by(id="3").first()
		xupdatep.quantity = Products.quantity + data.quantity
		xupdatep.commit()


		return {'message':'wow!'}
from flask_restful import Resource, reqparse
from db import db
from sqlalchemy import update
from flask_sqlalchemy import SQLAlchemy
from models.Products import Products

class Registerproducts(Resource):

	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('pname',
			type=str,
			required=True,
			help="This field cannot be left blank!"
			)
		parser.add_argument('pprice',
			type=str,
			required=True,
			help="This field cannot be left blank!"
			)
		parser.add_argument('quantity',
			type=str,
			required=True,
			help="This field cannot be left blank!"
			)
		parser.add_argument('ptype',
			type=str,
			required=True,
			help="This field cannot be left blank!"
			)
		data = parser.parse_args()

		new_product = Products(
			pname=data.pname,
			pprice=data.pprice,
			quantity=data.quantity,
			ptype=data.ptype
			)
		new_product.insert()
		return {'message':'Product Registered!'}

class UpdateProduct(Resource):
	
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('id',
			type=str,
			)
		parser.add_argument('pprice',
			type=str,
			required=True,
			help="This field cannot be left blank!"
			)
		parser.add_argument('quantity',
			type=str,
			required=True,
			help="This field cannot be left blank!"
			)
		parser.add_argument('ptype',
			type=str,
			required=True,
			help="This field cannot be left blank!"
			)
		data = parser.parse_args()
		product = Products.getById(data.id)
		updatex = Products.query.filter_by(id=product.id).first()

		updatex.pprice= data.pprice
		updatex.quantity= data.quantity
		updatex.ptype= data.ptype
		updatex.commit()

		return {'message':'Product Updated!'}

	''' 	product = Products.getById(data.id)
		(
			product.pprice == data.pprice,
			product.quantity == data.quantity,
			product.ptype == data.ptype
		)
		product.insert()

		updated = Products (
			pprice=data.pprice,
			quantity=data.quantity,
			ptype= data.ptype
			)
		updated.insert() '''


		

class getproduct(Resource):

	def get(self, _id):
	
		product = Products.getById(_id)

		return product.json()

class deleteproduct(Resource):

	def delete(self , _id):
		parser = reqparse.RequestParser()
		parser.add_argument('id',
			type=str,
			)
		parser.add_argument('pprice',
			type=str,
			required=True,
			help="This field cannot be left blank!"
			)
		parser.add_argument('quantity',
			type=str,
			required=True,
			help="This field cannot be left blank!"
			)
		parser.add_argument('ptype',
			type=str,
			required=True,
			help="This field cannot be left blank!"
			)
		data = parser.parse_args()
		product = Products.getById(data.id)
		delprod = Products.query.filter_by(id = product.id)
		delprod.delete(product)
		delprod.commit()
		return {'message':'Product deleted!'}
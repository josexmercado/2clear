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
		updatex.id= data.id
		updatex.pprice= data.pprice
		updatex.quantity= data.quantity
		updatex.ptype= data.ptype
		updatex.commit()

		return {'message':'Product Updated!'}


class UpdateQuantity(Resource):
	
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('pname',
			type=str,
			)
		parser.add_argument('type',
			type=str,
			required=True,
			help="This field cannot be left blank!"
			)
		parser.add_argument('quantity',
			type=int,
			required=True,
			help="This field cannot be left blank!"
			)
		data = parser.parse_args()
		product = Products.getByName(data.pname)
		xupdatex = Products.query.filter_by(pname=product.pname).first()
		xupdatex.quantity = Products.quantity + data.quantity
		xupdatex.commit()

		return {'message':'Stocks recorded!'}

class UpdatexQuantity(Resource):
	
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('pname',
			type=str,
			)
		parser.add_argument('type',
			type=str,
			required=True,
			help="This field cannot be left blank!"
			)
		parser.add_argument('quantity',
			type=int,
			required=True,
			help="This field cannot be left blank!"
			)
		data = parser.parse_args()
		product = Products.getByName(data.pname)
		xupdatex = Products.query.filter_by(pname=product.pname).first()
		xupdatex.quantity = Products.quantity - data.quantity
		xupdatex.commit()

		return {'message':'Stocks recorded!'}
		

class getproduct(Resource):

	def get(self, _id):
	
		product = Products.getById(_id)

		return product.json()

class getproductname(Resource):

	def get(self, _pname):
	
		product = Products.getByName(_pname)

		return product.json()

class deleteproduct(Resource):

	def delete(self):
		parser = reqparse.RequestParser()
		parser.add_argument('id',
			type=str,
			)
		data = parser.parse_args()
		product = Products.getById(data.id)
		delprod = Products.query.filter_by(id = product.id).first()
		delprod.delete()
		delprod.commit()
		return {'message':'Product deleted!'}


class deliverproduct(Resource):
	
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('id',
			type=str,
			required=True,
			help="This field cannot be left blank!"
			)
		parser.add_argument('quantity',
			type=str,
			required=True,
			help="This field cannot be left blank!"
			)
		data = parser.parse_args()
		product = Products.getById(data.id)
		xupdatex = Products.query.filter_by(id=product.id).first()
		xupdatex.quantity= Products.quantity - data.quantity
		xupdatex.commit()

		return {'message':'wow!'}


class cancelorder(Resource):
	
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('pname',
			type=str,
			required=True,
			help="This field cannot be left blank!"
			)
		parser.add_argument('quantity',
			type=int,
			required=True,
			help="This field cannot be left blank!"
			)
		data = parser.parse_args()
		product = Products.getByName(data.pname)
		xupdatex = Products.query.filter_by(pname=product.pname).first()
		xupdatex.quantity= Products.quantity + data.quantity
		xupdatex.commit()

		return {'message':'wow!'}


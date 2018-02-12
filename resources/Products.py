from flask_restful import Resource, reqparse
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

		updated_product = Products(
			pprice=data.pprice,
			quantity=data.quantity,
			ptype=data.ptype
			)
		updated_product.insert()
		return {'message':'Product Updated!'}


class getproduct(Resource):

	def get(self, _id):
	
		product = Products.getById(_id)

		return product.json()

class deleteproduct(Resource):

	def delete(self, _id):
	
		product = Products.delete(_id)

		return product.json()
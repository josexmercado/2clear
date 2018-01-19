from flask_restful import Resource, reqparse
from models.Products import Products

class Registerproducts(Resource):

	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('productname',
			type=str,
			required=True,
			help="This field cannot be left blank!"
			)
		parser.add_argument('productprice',
			type=str,
			required=True,
			help="This field cannot be left blank!"
			)
		parser.add_argument('productquantity',
			type=str,
			required=True,
			help="This field cannot be left blank!"
			)
		data = parser.parse_args()

		new_product = Products(
			pname=data.productname,
			pprice=data.productprice,
			quantity=data.productquantity
			)
		new_product.insert()
		return {'message':'Product Registered!'}
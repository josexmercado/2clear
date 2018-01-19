from flask_restful import Resource, reqparse
from models.Rproducts import Rproducts

class Registerrentalproducts(Resource):

	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('rproductname',
			type=str,
			required=True,
			help="This field cannot be left blank!"
			)
		parser.add_argument('rprice',
			type=str,
			required=True,
			help="This field cannot be left blank!"
			)
		parser.add_argument('rquantity',
			type=str,
			required=True,
			help="This field cannot be left blank!"
			)
		data = parser.parse_args()

		new_rproducts = Rproducts(
			rproductname=data.rproductname,
			rprice=data.rprice,
			rquantity=data.rquantity
			)
		new_rproducts.insert()
		return {'message':'Product Registered!'}
from flask_restful import Resource, reqparse
from models.CustomerModel import CustomerModel

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
		data = parser.parse_args()

		new_customer = CustomerModel(
			name=data.customername,
			address=data.customeraddress,
			number=data.customercontact
			)
		new_customer.insert()
		return {'message':'Customer added!'}

class CustomerData(Resource):

	def get(self, _id):
	
		customer = CustomerModel.getById(_id)

		return customer.json()
from flask_restful import Resource
from models.CustomerModel import CustomerModel

class Customer(Resource):

	def get(self, _id):

		customer = CustomerModel.getById(_id)

		return customer.json()
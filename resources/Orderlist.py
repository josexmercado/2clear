from flask_restful import Resource, reqparse
from models.Orders import Orders
from models.Orderlist import Orderlist

class getorderlist(Resource):

	def get(self, _id):
	
		orderlist = Orderlist.getById(_id)

		return [order.json() for order in orderlist]

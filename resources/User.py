from flask_restful import Resource, reqparse
from models.User import User

class UserRegister(Resource):

	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('username',
			type=str,
			required=True,
			help="This field cannot be left blank!"
			)
		parser.add_argument('password',
			type=str,
			required=True,
			help="This field cannot be left blank!"
			)
		parser.add_argument('name',
			type=str,
			required=True,
			help="This field cannot be left blank!"
			)
		data = parser.parse_args()
		if( User.find_by_username(data.username)):
			return {'message': 'Username is already taken.'}
		else:
			new_user = User(
				username=data.username,
				password=data.password,
				name=data.name
				)
			new_user.insert()
			return {'message':'User added!'}
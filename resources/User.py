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
		parser.add_argument('role',
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
				name=data.name,
				role=data.role
				)
			new_user.insert()
			return {'message':'User added!'}
class getuname(Resource):

	def get(self, _id):
	
		id = User.getByid(_id)

		return id.json()

class UpdateUser(Resource):
	
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('name',
			type=str,
			)
		parser.add_argument('id',
			type=str,
			required=True,
			help="This field cannot be left blank!"
			)
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
		parser.add_argument('role',
			type=str,
			required=True,
			help="This field cannot be left blank!"
			)
		data = parser.parse_args()
		product = User.getByName(data.name)
		updatex = User.query.filter_by(name=product.name).first()
		updatex.name= data.name
		updatex.username= data.username
		updatex.password= data.password
		updatex.role= data.role
		updatex.commit()

		return {'message':'Product Updated!'}

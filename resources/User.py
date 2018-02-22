from flask_restful import Resource, reqparse
from db import db
from sqlalchemy import update
from flask_sqlalchemy import SQLAlchemy
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
class getname(Resource):

	def get(self, _id):
	
		u = User.getUserId(_id)

		return u.json()

class UpdateUser(Resource):
	
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('id',
			type=str,
			)
		parser.add_argument('name',
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
		xuser = User.getUserId(data.id)
		upUser = User.query.filter_by(id=xuser.id).first()
		upUser.name = data.name
		upUser.username = data.username
		upUser.password = data.password
		upUser.role = data.role
		upUser.commit()

		return {'message':'User Updated!'}

class DeleteUser(Resource):

	def delete(self):
		parser = reqparse.RequestParser()
		parser.add_argument('id',
			type=str,
			)
		data = parser.parse_args()
		product = User.getUserId(data.id)
		delprod = User.query.filter_by(id = product.id).first()
		delprod.delete()
		delprod.commit()
		return {'message':'User deleted!'}


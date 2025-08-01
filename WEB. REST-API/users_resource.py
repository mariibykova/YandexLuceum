from flask_restful import Resource, reqparse
from models import User

class UsersResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('email', type=str, required=True, help="This field cannot be left blank!")

    def get(self, user_id):
        user = User.find_by_id(user_id)
        if user:
            return user.json()
        return {'message': 'User not found'}, 404

    def delete(self, user_id):
        user = User.find_by_id(user_id)
        if user:
            user.delete_from_db()
            return {'message': 'User deleted.'}
        return {'message': 'User not found'}, 404

    def put(self, user_id):
        data = UsersResource.parser.parse_args()
        user = User.find_by_id(user_id)
        if user:
            user.username = data['username']
            user.email = data['email']
            user.save_to_db()
            return user.json()
        return {'message': 'User not found'}, 404

class UsersListResource(Resource):
    def get(self):
        return {'users': [user.json() for user in User.query.all()]}

    def post(self):
        data = UsersResource.parser.parse_args()
        if User.find_by_username(data['username']):
            return {'message': "A user with that username already exists"}, 400
        user = User(**data)
        user.save_to_db()
        return user.json(), 201

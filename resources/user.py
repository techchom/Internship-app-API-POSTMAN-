from flask_restful import Resource, reqparse
from models.user import UserModel
from flask_jwt_extended import create_access_token

parser = reqparse.RequestParser()
parser.add_argument('username', type=str, required=True)
parser.add_argument('password', type=str, required=True)

class UserRegister(Resource):
    def post(self):
        data = parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {"message": "User already exists."}, 400
        user = UserModel(**data)
        user.save_to_db()
        return {"message": "User registered successfully."}, 201

class UserLogin(Resource):
    def post(self):
        print("POST /login called")  # debug
        data = parser.parse_args()
        user = UserModel.find_by_username(data['username'])
        if user and user.password == data['password']:
            token = create_access_token(identity=str(user.id))
            return {"access_token": token}, 200
        return {"message": "Invalid credentials"}, 401


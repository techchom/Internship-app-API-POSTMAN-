from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from models.university import UniversityModel

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True, help='Name cannot be blank!')

class University(Resource):
    @jwt_required()
    def post(self):
        data = parser.parse_args()
        if UniversityModel.find_by_name(data['name']):
            return {'message': 'University already exists'}, 400
        university = UniversityModel(name=data['name'])
        university.save_to_db()
        return {'message': 'University created successfully.'}, 201

    @jwt_required()
    def put(self, id):
        data = parser.parse_args()
        university = UniversityModel.query.get(id)
        if not university:
            return {'message': 'University not found'}, 404
        university.name = data['name']
        university.save_to_db()
        return {'message': 'University updated successfully.'}, 200

    @jwt_required()
    def delete(self, id):
        university = UniversityModel.query.get(id)
        if not university:
            return {'message': 'University not found'}, 404
        university.delete_from_db()
        return {'message': 'University deleted successfully.'}, 200

    def get(self, id):
        university = UniversityModel.query.get(id)
        if not university:
            return {'message': 'University not found'}, 404
        return {
            'id': university.id,
            'name': university.name,
            'interns': [intern.id for intern in university.interns]
        }, 200

class UniversityList(Resource):
    def get(self):
        universities = UniversityModel.query.all()
        return {'universities': [
            {
                'id': u.id,
                'name': u.name,
                'interns': [intern.id for intern in u.interns]
            } for u in universities
        ]}, 200

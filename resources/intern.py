from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from models.intern import InternModel

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True, help="This field cannot be blank.")
parser.add_argument('description', type=str)
parser.add_argument('university_id', type=int, required=True)

class Intern(Resource):
    @jwt_required()
    def post(self):
        data = parser.parse_args()
        intern = InternModel(**data)
        intern.save_to_db()
        return {"message": "Intern created."}, 201

    def get(self, id):
        intern = InternModel.query.get(id)
        if not intern:
            return {"message": "Intern not found."}, 404
        return {
            "id": intern.id,
            "name": intern.name,
            "description": intern.description,
            "university_id": intern.university_id
        }

    @jwt_required()
    def put(self, id):
        data = parser.parse_args()
        intern = InternModel.query.get(id)
        if not intern:
            return {"message": "Intern not found."}, 404
        intern.name = data["name"]
        intern.description = data["description"]
        intern.university_id = data["university_id"]
        intern.save_to_db()
        return {"message": "Intern updated."}

    @jwt_required()
    def delete(self, id):
        intern = InternModel.query.get(id)
        if not intern:
            return {"message": "Intern not found."}, 404
        intern.delete_from_db()
        return {"message": "Intern deleted."}

class InternList(Resource):
    def get(self):
        return {
            "interns": [
                {
                    "id": i.id,
                    "name": i.name,
                    "description": i.description,
                    "university_id": i.university_id
                } for i in InternModel.query.all()
            ]
        }

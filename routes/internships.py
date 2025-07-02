from flask import Blueprint, request, jsonify, render_template
from models.intern import InternModel
from models.university import UniversityModel
from models.db import db

internship_bp = Blueprint("internship_bp", __name__)

# Home route brenda blueprint-it (opsionale)
@internship_bp.route('/')
def bp_home():
    return jsonify({"message": "Welcome to Internship API from blueprint"})

# List all internships
@internship_bp.route('/internships', methods=['GET'])
def list_internships():
    internships = InternModel.query.all()
    result = []
    for i in internships:
        result.append({
            "id": i.id,
            "name": i.name,
            "description": i.description,
            "university_id": i.university_id
        })
    return jsonify({"internships": result}), 200

# Create a new internship
@internship_bp.route('/internships', methods=['POST'])
def create_internship():
    data = request.get_json()
    required_fields = ["name", "university_id"]

    for field in required_fields:
        if not data.get(field):
            return jsonify({"error": f"Missing required field: {field}"}), 400

    university = UniversityModel.query.get(data['university_id'])
    if not university:
        return jsonify({"error": "University not found"}), 404

    internship = InternModel(
        name=data['name'],
        university_id=data['university_id'],
        description=data.get('description')
    )
    internship.save_to_db()
    return jsonify({"message": "Internship created successfully."}), 201

# Update internship by ID
@internship_bp.route('/internships/<int:id>', methods=['PUT'])
def update_internship(id):
    data = request.get_json()
    internship = InternModel.query.get(id)

    if not internship:
        return jsonify({"error": "Internship not found"}), 404

    internship.name = data.get("name", internship.name)
    internship.description = data.get("description", internship.description)
    internship.university_id = data.get("university_id", internship.university_id)

    db.session.commit()
    return jsonify({"message": "Internship updated successfully."}), 200

# Delete internship by ID
@internship_bp.route('/internships/<int:id>', methods=['DELETE'])
def delete_internship(id):
    internship = InternModel.query.get(id)
    if not internship:
        return jsonify({"error": "Internship not found"}), 404

    internship.delete_from_db()
    return jsonify({"message": "Internship deleted successfully."}), 200

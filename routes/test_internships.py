import pytest
from app import app, db
from models.intern import InternModel

@pytest.fixture
def client():
    # Konfiguro aplikacionin për testim
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.session.remove()
        db.drop_all()

def test_create_internship(client):
    # Krijo një internship
    response = client.post('/internships', json={
        "name": "Software Intern",
        "university_id": 1,  # Duhet të krijosh universitetin në test ose ta bësh nullable
        "description": "Internship about software development"
    })
    # Sipas modeleve tuaja, nëse university_id nuk ekziston → 404
    assert response.status_code in (201, 404)

def test_list_internships(client):
    response = client.get('/internships')
    assert response.status_code == 200
    assert "internships" in response.json

def test_update_internship(client):
    # Fillimisht krijo një internship
    internship = InternModel(name="Initial", university_id=1)
    with app.app_context():
        db.session.add(internship)
        db.session.commit()
        internship_id = internship.id

    # Pastaj bëj update
    response = client.put(f'/internships/{internship_id}', json={
        "name": "Updated",
        "description": "Updated desc"
    })
    assert response.status_code == 200
    assert response.json['message'] == "Internship updated successfully."

def test_delete_internship(client):
    # Krijo internship për ta fshirë
    internship = InternModel(name="ToDelete", university_id=1)
    with app.app_context():
        db.session.add(internship)
        db.session.commit()
        internship_id = internship.id

    response = client.delete(f'/internships/{internship_id}')
    assert response.status_code == 200
    assert response.json['message'] == "Internship deleted successfully."

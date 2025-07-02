import unittest
import json
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app, db
from models.user import UserModel
from models.intern import InternModel
from models.university import UniversityModel

class TestIntegration(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['TESTING'] = True
        app.config['JWT_SECRET_KEY'] = 'test-secret'
        self.app = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_user_registration_and_login(self):
        """Test complete user registration and login workflow"""
        # Register user
        response = self.app.post('/register',
                               data=json.dumps({'username': 'testuser', 'password': 'testpass'}),
                               content_type='application/json')
        self.assertEqual(response.status_code, 201)
        
        # Login user
        response = self.app.post('/login',
                               data=json.dumps({'username': 'testuser', 'password': 'testpass'}),
                               content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('access_token', data)

    def test_protected_endpoints_authentication(self):
        """Test that protected endpoints require authentication"""
        # Try to create university without token
        response = self.app.post('/university',
                               data=json.dumps({'name': 'Test University'}),
                               content_type='application/json')
        self.assertEqual(response.status_code, 401)
        
        # Try to create intern without token
        response = self.app.post('/intern',
                               data=json.dumps({
                                   'name': 'Test Intern',
                                   'university_id': 1,
                                   'description': 'Test description'
                               }),
                               content_type='application/json')
        self.assertEqual(response.status_code, 401)

    def test_basic_api_endpoints(self):
        """Test basic API endpoints without authentication"""
        # Test home endpoint
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        
        # Test universities endpoint
        response = self.app.get('/universities')
        self.assertEqual(response.status_code, 200)
        
        # Test interns endpoint
        response = self.app.get('/interns')
        self.assertEqual(response.status_code, 200)

    def test_model_integration(self):
        """Test integration between models using direct database operations"""
        with app.app_context():
            # Create university directly
            university = UniversityModel(name='Test University')
            university.save_to_db()
            
            # Create intern directly
            intern = InternModel(
                name='Test Intern',
                university_id=1,
                description='Test description'
            )
            intern.save_to_db()
            
            # Test that both exist
            found_university = UniversityModel.find_by_name('Test University')
            self.assertIsNotNone(found_university)
            
            found_intern = InternModel.find_by_name('Test Intern')
            self.assertIsNotNone(found_intern)
            if found_intern:  # Type guard
                self.assertEqual(found_intern.university_id, 1)

if __name__ == '__main__':
    unittest.main()
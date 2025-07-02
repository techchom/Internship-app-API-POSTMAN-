import unittest
import json
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app, db

class TestSystem(unittest.TestCase):
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

    def test_api_endpoints_availability(self):
        """Test that all required API endpoints are available"""
        # Test home endpoint
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        
        # Test register endpoint
        response = self.app.post('/register',
                               data=json.dumps({'username': 'testuser', 'password': 'testpass'}),
                               content_type='application/json')
        self.assertEqual(response.status_code, 201)
        
        # Test login endpoint
        response = self.app.post('/login',
                               data=json.dumps({'username': 'testuser', 'password': 'testpass'}),
                               content_type='application/json')
        self.assertEqual(response.status_code, 200)
        
        # Test universities endpoint
        response = self.app.get('/universities')
        self.assertEqual(response.status_code, 200)
        
        # Test interns endpoint
        response = self.app.get('/interns')
        self.assertEqual(response.status_code, 200)

    def test_error_handling(self):
        """Test system error handling"""
        # Test invalid login
        response = self.app.post('/login',
                               data=json.dumps({'username': 'nonexistent', 'password': 'wrong'}),
                               content_type='application/json')
        self.assertEqual(response.status_code, 401)
        
        # Test duplicate user registration
        self.app.post('/register',
                     data=json.dumps({'username': 'testuser', 'password': 'testpass'}),
                     content_type='application/json')
        
        response = self.app.post('/register',
                               data=json.dumps({'username': 'testuser', 'password': 'testpass'}),
                               content_type='application/json')
        self.assertEqual(response.status_code, 400)
        
        # Test accessing non-existent resource
        response = self.app.get('/intern/999')
        self.assertEqual(response.status_code, 404)

    def test_basic_workflow(self):
        """Test basic workflow without complex JWT authentication"""
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

if __name__ == '__main__':
    unittest.main()
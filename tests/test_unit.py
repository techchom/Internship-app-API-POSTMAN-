import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app, db
from models.user import UserModel
from models.intern import InternModel
from models.university import UniversityModel

class TestModels(unittest.TestCase):
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

    def test_user_model(self):
        """Test UserModel functionality"""
        with app.app_context():
            # Test user creation
            user = UserModel(username='testuser', password='testpass')
            user.save_to_db()
            
            # Test find_by_username
            found_user = UserModel.find_by_username('testuser')
            self.assertIsNotNone(found_user)
            if found_user:  # Type guard
                self.assertEqual(found_user.username, 'testuser')
            
            # Test find_by_id
            found_user_by_id = UserModel.find_by_id(1)
            self.assertIsNotNone(found_user_by_id)
            if found_user_by_id:  # Type guard
                self.assertEqual(found_user_by_id.username, 'testuser')

    def test_university_model(self):
        """Test UniversityModel functionality"""
        with app.app_context():
            # Test university creation
            university = UniversityModel(name='Test University')
            university.save_to_db()
            
            # Test find_by_name
            found_university = UniversityModel.find_by_name('Test University')
            self.assertIsNotNone(found_university)
            if found_university:  # Type guard
                self.assertEqual(found_university.name, 'Test University')
            
            # Test delete_from_db
            university.delete_from_db()
            found_university = UniversityModel.find_by_name('Test University')
            self.assertIsNone(found_university)

    def test_intern_model(self):
        """Test InternModel functionality"""
        with app.app_context():
            # Create university first
            university = UniversityModel(name='Test University')
            university.save_to_db()
            
            # Test intern creation with description
            intern = InternModel(
                name='Test Intern',
                university_id=1,
                description='Test internship description'
            )
            intern.save_to_db()
            
            # Test find_by_name
            found_intern = InternModel.find_by_name('Test Intern')
            self.assertIsNotNone(found_intern)
            if found_intern:  # Type guard
                self.assertEqual(found_intern.name, 'Test Intern')
                self.assertEqual(found_intern.description, 'Test internship description')
            
            # Test delete_from_db
            intern.delete_from_db()
            found_intern = InternModel.find_by_name('Test Intern')
            self.assertIsNone(found_intern)

    def test_intern_university_foreign_key(self):
        """Test that intern has correct university_id"""
        with app.app_context():
            # Create university
            university = UniversityModel(name='Test University')
            university.save_to_db()
            
            # Create intern
            intern = InternModel(
                name='Test Intern',
                university_id=1,
                description='Test description'
            )
            intern.save_to_db()
            
            # Test that the foreign key is set correctly
            self.assertEqual(intern.university_id, 1)

    def test_description_field(self):
        """Test that the description field works correctly"""
        with app.app_context():
            # Create university
            university = UniversityModel(name='Test University')
            university.save_to_db()
            
            # Create intern with description
            intern = InternModel(
                name='Test Intern',
                university_id=1,
                description='This is a test internship description'
            )
            intern.save_to_db()
            
            # Verify description is saved
            found_intern = InternModel.find_by_name('Test Intern')
            self.assertIsNotNone(found_intern)
            if found_intern:  # Type guard
                self.assertEqual(found_intern.description, 'This is a test internship description')
            
            # Test intern without description
            intern2 = InternModel(
                name='Test Intern 2',
                university_id=1
            )
            intern2.save_to_db()
            
            found_intern2 = InternModel.find_by_name('Test Intern 2')
            self.assertIsNotNone(found_intern2)
            if found_intern2:  # Type guard
                self.assertIsNone(found_intern2.description)

if __name__ == '__main__':
    unittest.main()
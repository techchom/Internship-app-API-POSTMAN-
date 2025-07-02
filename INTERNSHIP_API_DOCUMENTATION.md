# Internship Management API - Complete Documentation

## Project Overview

This project is a **Flask REST API** for managing internships with comprehensive user authentication, university management, and intern tracking capabilities. The system was built from scratch and includes full testing coverage.

## Technology Stack

- **Backend Framework**: Flask
- **Database**: SQLite with SQLAlchemy ORM
- **Authentication**: JWT (JSON Web Tokens)
- **API Framework**: Flask-RESTful
- **Testing**: pytest (Unit, Integration, System tests)
- **API Testing**: Postman Collection
- **Language**: Python 3.x

## Project Structure

```
internship_app/
├── app.py                          # Main Flask application
├── requirements.txt                # Python dependencies
├── models/                         # Database models
│   ├── __init__.py
│   ├── db.py                      # Database configuration
│   ├── user.py                    # User model
│   ├── university.py              # University model
│   └── intern.py                  # Intern model
├── resources/                      # API resources/endpoints
│   ├── __init__.py
│   ├── user.py                    # User endpoints
│   ├── university.py              # University endpoints
│   └── intern.py                  # Intern endpoints
├── routes/                         # Route definitions
│   ├── __init__.py
│   ├── internships.py
│   └── test_internships.py
├── tests/                          # Test suite
│   ├── __init__.py
│   ├── test_unit.py               # Unit tests
│   ├── test_integration.py        # Integration tests
│   ├── test_system.py             # System tests
│   └── mocks/
│       └── mock_data.py           # Mock data for tests
├── templates/                      # HTML templates
│   ├── index.html
│   └── apply.html
├── instance/                       # Database files
│   └── data.db
├── postman_collection.json         # Postman API collection
├── postman_environment.json        # Postman environment variables
├── test_api.py                     # API testing script
├── test_curl.sh                    # cURL testing script
└── settings.json                   # Application settings
```

## What We Built - Complete Feature List

### 1. Database Models
- **User Model**: Handles user registration, authentication, and profile management
- **University Model**: Manages university information and relationships
- **Intern Model**: Tracks intern details, applications, and university relationships

### 2. Authentication System
- JWT-based authentication
- User registration and login endpoints
- Protected routes requiring authentication
- Token-based session management

### 3. API Endpoints

#### User Management
- `POST /register` - User registration
- `POST /login` - User authentication
- `GET /users` - List all users (admin only)
- `GET /user/<id>` - Get specific user
- `PUT /user/<id>` - Update user
- `DELETE /user/<id>` - Delete user

#### University Management
- `POST /university` - Create university
- `GET /universities` - List all universities
- `GET /university/<id>` - Get specific university
- `PUT /university/<id>` - Update university
- `DELETE /university/<id>` - Delete university

#### Intern Management
- `POST /intern` - Create intern profile
- `GET /interns` - List all interns
- `GET /intern/<id>` - Get specific intern
- `PUT /intern/<id>` - Update intern
- `DELETE /intern/<id>` - Delete intern

### 4. Testing Suite
- **Unit Tests**: Individual component testing
- **Integration Tests**: API endpoint testing
- **System Tests**: End-to-end workflow testing
- **Postman Collection**: Manual API testing
- **cURL Scripts**: Command-line API testing

## Installation and Setup Instructions

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)
- Git (optional, for version control)

### Step 1: Clone or Download the Project
```bash
# If using Git
git clone <repository-url>
cd internship_app

# Or download and extract the project files
```

### Step 2: Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Initialize Database
```bash
# The database will be automatically created when you first run the application
python app.py
```

## How to Run the Application

### Method 1: Direct Python Execution
```bash
# Make sure virtual environment is activated
python app.py
```

### Method 2: Flask Development Server
```bash
# Set Flask environment variables
set FLASK_APP=app.py
set FLASK_ENV=development

# Run Flask
flask run
```

The application will start on `http://127.0.0.1:5000`

## Testing Instructions

### 1. Run All Tests
```bash
# Run all tests with coverage
python -m pytest tests/ -v

# Run specific test files
python -m pytest tests/test_unit.py -v
python -m pytest tests/test_integration.py -v
python -m pytest tests/test_system.py -v
```

### 2. API Testing with cURL
```bash
# Run the provided cURL test script
bash test_curl.sh

# Or run the Python API test script
python test_api.py
```

### 3. Postman Testing
1. Open Postman
2. Import `postman_collection.json`
3. Import `postman_environment.json`
4. Set the environment variables
5. Run the collection tests

## API Usage Examples

### Authentication Flow
```bash
# 1. Register a new user
curl -X POST http://127.0.0.1:5000/register \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "password123", "email": "test@example.com"}'

# 2. Login to get JWT token
curl -X POST http://127.0.0.1:5000/login \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "password123"}'

# 3. Use the token for authenticated requests
curl -X GET http://127.0.0.1:5000/universities \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"
```

### University Management
```bash
# Create university
curl -X POST http://127.0.0.1:5000/university \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -d '{"name": "MIT", "location": "Cambridge, MA"}'

# Get all universities
curl -X GET http://127.0.0.1:5000/universities \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"
```

### Intern Management
```bash
# Create intern profile
curl -X POST http://127.0.0.1:5000/intern \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -d '{"name": "John Doe", "email": "john@example.com", "university_id": 1}'

# Get all interns
curl -X GET http://127.0.0.1:5000/interns \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"
```

## Key Features Implemented

### 1. Database Relationships
- Users can be associated with multiple universities
- Interns are linked to universities
- Proper foreign key constraints and cascading deletes

### 2. Security Features
- Password hashing using bcrypt
- JWT token authentication
- Protected routes requiring authentication
- Input validation and sanitization

### 3. Error Handling
- Comprehensive error responses
- Proper HTTP status codes
- Detailed error messages for debugging

### 4. Data Validation
- Required field validation
- Email format validation
- Unique constraint enforcement
- Data type validation

## Troubleshooting Common Issues

### 1. Database Errors
- **Issue**: "NOT NULL constraint failed"
- **Solution**: Ensure all required fields are provided in API requests

### 2. Authentication Errors
- **Issue**: "401 Unauthorized"
- **Solution**: Include valid JWT token in Authorization header

### 3. Import Errors
- **Issue**: "Module not found"
- **Solution**: Ensure virtual environment is activated and dependencies are installed

### 4. Port Already in Use
- **Issue**: "Address already in use"
- **Solution**: Change port in app.py or kill existing process

## Development Workflow

### 1. Making Changes
1. Activate virtual environment
2. Make code changes
3. Run tests to ensure functionality
4. Test API endpoints manually
5. Commit changes

### 2. Adding New Features
1. Create model if needed
2. Add resource endpoints
3. Update routes
4. Write tests
5. Update documentation

### 3. Database Migrations
- The current setup uses SQLite with automatic table creation
- For production, consider using Flask-Migrate for database migrations

## Production Deployment Considerations

### 1. Security
- Use environment variables for sensitive data
- Enable HTTPS
- Implement rate limiting
- Add request logging

### 2. Database
- Use PostgreSQL or MySQL for production
- Implement database migrations
- Set up database backups

### 3. Performance
- Use a production WSGI server (Gunicorn, uWSGI)
- Implement caching (Redis)
- Add database connection pooling

## Project Achievements

✅ **Complete REST API** with all CRUD operations  
✅ **JWT Authentication** system  
✅ **Comprehensive Testing** (Unit, Integration, System)  
✅ **Database Models** with proper relationships  
✅ **API Documentation** and testing tools  
✅ **Error Handling** and validation  
✅ **Postman Collection** for manual testing  
✅ **cURL Scripts** for command-line testing  

## Next Steps and Enhancements

1. **Frontend Development**: Create a web interface
2. **Email Notifications**: Add email functionality
3. **File Upload**: Support for resume/CV uploads
4. **Advanced Search**: Implement filtering and search
5. **Reporting**: Add analytics and reporting features
6. **Mobile App**: Develop mobile application
7. **Deployment**: Deploy to cloud platform

## Support and Maintenance

- Monitor application logs for errors
- Regularly update dependencies
- Backup database regularly
- Monitor API performance
- Keep documentation updated

---

**Project Status**: ✅ **COMPLETE**  
**Last Updated**: July 2025  
**Version**: 1.0.0  
**Author**: Internship Management API Team 
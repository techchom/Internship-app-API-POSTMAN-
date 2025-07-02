# Internship Management API

A RESTful API for managing internships using Flask, SQLAlchemy, and Flask-RESTful with JWT authentication.

## Features

- User registration and authentication with JWT
- University management (CRUD operations)
- Intern management with description field
- Protected endpoints for POST, PUT, DELETE operations
- SQLite database for development
- Comprehensive testing suite

## Project Structure

```
internship_app/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── models/
│   ├── db.py             # SQLAlchemy database setup
│   ├── user.py           # UserModel
│   ├── intern.py         # InternModel with description field
│   └── university.py     # UniversityModel
├── resources/
│   ├── user.py           # User registration and login
│   ├── intern.py         # Intern CRUD operations
│   └── university.py     # University CRUD operations
├── tests/
│   ├── test_unit.py      # Unit tests for models
│   ├── test_integration.py # Integration tests
│   └── test_system.py    # System tests
└── README.md/            # Documentation
```

## Setup Instructions

### 1. Virtual Environment Setup

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
python app.py
```

The application will run on `http://localhost:5000`

## API Endpoints

### Authentication

#### Register User
- **POST** `/register`
- **Body:**
```json
{
    "username": "testuser",
    "password": "testpass123"
}
```

#### Login User
- **POST** `/login`
- **Body:**
```json
{
    "username": "testuser",
    "password": "testpass123"
}
```
- **Response:** Returns JWT access token

### Universities

#### Get All Universities
- **GET** `/universities`
- **Authentication:** Not required

#### Get University by ID
- **GET** `/university/{id}`
- **Authentication:** Not required

#### Create University
- **POST** `/university`
- **Authentication:** Required (JWT)
- **Body:**
```json
{
    "name": "MIT University"
}
```

#### Update University
- **PUT** `/university/{id}`
- **Authentication:** Required (JWT)
- **Body:**
```json
{
    "name": "Updated University Name"
}
```

#### Delete University
- **DELETE** `/university/{id}`
- **Authentication:** Required (JWT)

### Interns

#### Get All Interns
- **GET** `/interns`
- **Authentication:** Not required

#### Get Intern by ID
- **GET** `/intern/{id}`
- **Authentication:** Not required

#### Create Intern
- **POST** `/intern`
- **Authentication:** Required (JWT)
- **Body:**
```json
{
    "name": "John Doe",
    "university_id": 1,
    "description": "Software Engineering Internship"
}
```

#### Update Intern
- **PUT** `/intern/{id}`
- **Authentication:** Required (JWT)
- **Body:**
```json
{
    "name": "John Doe Updated",
    "university_id": 1,
    "description": "Updated internship description"
}
```

#### Delete Intern
- **DELETE** `/intern/{id}`
- **Authentication:** Required (JWT)

## Testing

### Running Tests

#### Unit Tests
```bash
python -m unittest tests.test_unit
```

#### Integration Tests
```bash
python -m unittest tests.test_integration
```

#### System Tests
```bash
python -m unittest tests.test_system
```

#### All Tests
```bash
python -m unittest discover tests
```

### Postman Testing

1. **Import the provided Postman collection**
2. **Set up environment variables:**
   - `base_url`: `http://localhost:5000`
   - `access_token`: (will be set automatically after login)

3. **Test Workflow:**
   - Register a new user
   - Login to get JWT token
   - Create a university
   - Create an intern with description
   - Test all CRUD operations
   - Verify the description field is included

## Database Schema

### Users Table
- `id` (Primary Key)
- `username` (Unique)
- `password` (Hashed)

### Universities Table
- `id` (Primary Key)
- `name` (Unique)

### Interns Table
- `id` (Primary Key)
- `name`
- `university_id` (Foreign Key)
- `description` (Text field for internship description)

## Authentication

The API uses JWT (JSON Web Tokens) for authentication. Protected endpoints require the JWT token in the Authorization header:

```
Authorization: Bearer <your_jwt_token>
```

## Additional Features

### Description Field
The InternModel includes a `description` field as required by the assignment. This field stores text descriptions of internships and is included in all API responses.

### Error Handling
The API includes comprehensive error handling for:
- Missing required fields
- Invalid credentials
- Resource not found
- Duplicate entries
- Authentication failures

## Development Notes

- The application uses SQLite for development
- JWT secret key should be changed in production
- All models include the required methods as specified in the assignment
- The API follows RESTful conventions
- Comprehensive test coverage is provided

## Screenshots

Include screenshots of:
1. Passing Postman tests
2. Successful API responses
3. Test execution results
4. Database schema verification 
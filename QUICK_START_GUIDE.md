# Quick Start Guide - Internship Management API

## 🚀 Get Started in 5 Minutes

### 1. Setup Environment
```bash
# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt
```

### 2. Run the Application
```bash
python app.py
```
The API will be available at: `http://127.0.0.1:5000`

### 3. Test the API
```bash
# Run the quick test script
python test_api.py

# Or use cURL
bash test_curl.sh
```

## 🔑 Quick Authentication Test

```bash
# 1. Register a user
curl -X POST http://127.0.0.1:5000/register \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "password123", "email": "test@example.com"}'

# 2. Login to get token
curl -X POST http://127.0.0.1:5000/login \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "password123"}'

# 3. Use the token (replace YOUR_TOKEN with the actual token)
curl -X GET http://127.0.0.1:5000/universities \
  -H "Authorization: Bearer YOUR_TOKEN"
```

## 📋 Available Endpoints

### Public Endpoints
- `POST /register` - Create account
- `POST /login` - Get authentication token

### Protected Endpoints (require JWT token)
- `GET /universities` - List universities
- `POST /university` - Create university
- `GET /interns` - List interns
- `POST /intern` - Create intern profile

## 🧪 Run Tests
```bash
# All tests
python -m pytest tests/ -v

# Specific test types
python -m pytest tests/test_unit.py -v
python -m pytest tests/test_integration.py -v
```

## 📚 Full Documentation
See `INTERNSHIP_API_DOCUMENTATION.md` for complete details.

---
**Need Help?** Check the troubleshooting section in the main documentation. 
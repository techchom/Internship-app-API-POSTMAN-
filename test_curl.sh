#!/bin/bash
# Simple curl tests for the Internship API

BASE_URL="http://localhost:5000"

echo "🧪 Testing Internship API with curl..."
echo "=================================================="

# Test 1: Home page
echo "1. Testing home page..."
curl -X GET "$BASE_URL/" -H "Content-Type: application/json"
echo -e "\n"

# Test 2: Register user
echo "2. Testing user registration..."
curl -X POST "$BASE_URL/register" \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "testpass123"}'
echo -e "\n"

# Test 3: Login user
echo "3. Testing user login..."
TOKEN=$(curl -s -X POST "$BASE_URL/login" \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "testpass123"}' | \
  python -c "import sys, json; print(json.load(sys.stdin)['access_token'])")
echo "Token: $TOKEN"

# Test 4: Create university
echo "4. Testing university creation..."
curl -X POST "$BASE_URL/university" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"name": "MIT University"}'
echo -e "\n"

# Test 5: Create intern
echo "5. Testing intern creation..."
curl -X POST "$BASE_URL/intern" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"name": "John Doe", "university_id": 1, "description": "Software Engineering Internship"}'
echo -e "\n"

# Test 6: Get all interns
echo "6. Testing get all interns..."
curl -X GET "$BASE_URL/interns" -H "Content-Type: application/json"
echo -e "\n"

echo "=================================================="
echo "🎉 curl testing completed!" 
#!/usr/bin/env python3
"""
Simple API test script to verify the internship API is working correctly.
Run this after starting your Flask app.
"""

import requests
import json

BASE_URL = "http://localhost:5000"

def test_api():
    print("🧪 Testing Internship API...")
    print("=" * 50)
    
    # Test 1: Home page
    print("1. Testing home page...")
    response = requests.get(f"{BASE_URL}/")
    if response.status_code == 200:
        print("✅ Home page works")
    else:
        print(f"❌ Home page failed: {response.status_code}")
    
    # Test 2: Register user
    print("2. Testing user registration...")
    user_data = {"username": "testuser", "password": "testpass123"}
    response = requests.post(f"{BASE_URL}/register", json=user_data)
    if response.status_code == 201:
        print("✅ User registration works")
    else:
        print(f"❌ User registration failed: {response.status_code}")
    
    # Test 3: Login user
    print("3. Testing user login...")
    response = requests.post(f"{BASE_URL}/login", json=user_data)
    if response.status_code == 200:
        token = response.json().get('access_token')
        print("✅ User login works")
        print(f"   Token received: {token[:20]}...")
    else:
        print(f"❌ User login failed: {response.status_code}")
        return
    
    # Test 4: Create university (with auth)
    print("4. Testing university creation...")
    headers = {"Authorization": f"Bearer {token}"}
    university_data = {"name": "MIT University"}
    response = requests.post(f"{BASE_URL}/university", json=university_data, headers=headers)
    if response.status_code == 201:
        print("✅ University creation works")
    else:
        print(f"❌ University creation failed: {response.status_code}")
        print(f"   Response: {response.text}")
    
    # Test 5: Create intern (with auth)
    print("5. Testing intern creation...")
    intern_data = {
        "name": "John Doe",
        "university_id": 1,
        "description": "Software Engineering Internship"
    }
    response = requests.post(f"{BASE_URL}/intern", json=intern_data, headers=headers)
    if response.status_code == 201:
        print("✅ Intern creation works")
    else:
        print(f"❌ Intern creation failed: {response.status_code}")
        print(f"   Response: {response.text}")
    
    # Test 6: Get all interns
    print("6. Testing get all interns...")
    response = requests.get(f"{BASE_URL}/interns")
    if response.status_code == 200:
        data = response.json()
        interns = data.get('interns', [])
        print(f"✅ Get interns works - Found {len(interns)} interns")
        if interns:
            intern = interns[0]
            if 'description' in intern:
                print(f"   ✅ Description field present: {intern['description']}")
            else:
                print("   ❌ Description field missing")
    else:
        print(f"❌ Get interns failed: {response.status_code}")
    
    # Test 7: Get all universities
    print("7. Testing get all universities...")
    response = requests.get(f"{BASE_URL}/universities")
    if response.status_code == 200:
        data = response.json()
        universities = data.get('universities', [])
        print(f"✅ Get universities works - Found {len(universities)} universities")
    else:
        print(f"❌ Get universities failed: {response.status_code}")
    
    print("=" * 50)
    print("🎉 API testing completed!")

if __name__ == "__main__":
    try:
        test_api()
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to the API. Make sure your Flask app is running on http://localhost:5000")
    except Exception as e:
        print(f"❌ Error during testing: {e}") 
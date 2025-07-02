from flask import Flask, jsonify, render_template
from flask_restful import Api
from flask_jwt_extended import JWTManager
from models.db import db
from resources.user import UserRegister, UserLogin
from resources.intern import Intern, InternList
from resources.university import University, UniversityList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret-key'

db.init_app(app)
jwt = JWTManager(app)
api = Api(app)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to Internship API"})

@app.route('/apply')
def apply_page():
    return render_template('apply.html')

# API endpoints
api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')
api.add_resource(Intern, '/intern/<int:id>', '/intern')
api.add_resource(InternList, '/interns')
api.add_resource(University, '/university/<int:id>', '/university')
api.add_resource(UniversityList, '/universities')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

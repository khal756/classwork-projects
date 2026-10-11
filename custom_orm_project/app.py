from flask import Flask, jsonify, request
from db import Database
from orm import User

app = Flask(__name__)

# Initialize our database and model
db = Database()
user_model = User(db)

@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Custom ORM API!"}), 200

@app.route("/users", methods=["GET"])
def get_users():
    """Route to fetch all users as JSON."""
    users = user_model.get_all_users()
    return jsonify(users), 200

@app.route("/users", methods=["POST"])
def create_user():
    """Route to receive JSON data and create a new user."""
    data = request.get_json()
    
    new_user = user_model.add_user(
        name=data.get('name'),
        email=data.get('email'),
        gender=data.get('gender'),
        age=data.get('age')
    )
    return jsonify({"message": "User added successfully", "user": new_user}), 201

if __name__ == "__main__":
    app.run(debug=True)
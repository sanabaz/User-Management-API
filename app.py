from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {"id": 1, "name": "Sandro", "age": 22},
    {"id": 2, "name": "Anna", "age": 24},
    {"id": 3, "name": "David", "age": 23},
    {"id": 4, "name": "Anush", "age": 25},
    {"id": 5, "name": "Marine", "age": 22}
]

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the User Management API!"})

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    if not data or "name" not in data or "age" not in data:
        return jsonify({"error": "Invalid input"}), 400
    new_id = max([u["id"] for u in users]) + 1 if users else 1
    new_user = {"id": new_id, "name": data["name"], "age": data["age"]}
    users.append(new_user)
    return jsonify(new_user), 201

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [u for u in users if u["id"] != user_id]
    return jsonify({"message": f"User with id {user_id} deleted"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
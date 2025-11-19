from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# In-memory user data
users = [
    {"id": 1, "name": "Amit", "email": "amit@example.com"},
    {"id": 2, "name": "Reena", "email": "reena@example.com"}
]

@app.route('/')
def home():
    return render_template('apiindex.html', users=users)

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    for u in users:
        if u["id"] == user_id:
            return jsonify(u)
    return jsonify({"error": "User not found"}), 404

@app.route('/users', methods=['POST'])
def add_user():
    new_user = request.json
    users.append(new_user)
    return jsonify({"message": "User added"}), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    for u in users:
        if u["id"] == user_id:
            u["name"] = data.get("name", u["name"])
            u["email"] = data.get("email", u["email"])
            return jsonify({"message": "User updated"})
    return jsonify({"error": "User not found"}), 404

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    for u in users:
        if u["id"] == user_id:
            users.remove(u)
            return jsonify({"message": "User deleted"})
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)

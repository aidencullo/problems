from flask import Flask, jsonify, request

app = Flask(__name__)


# GET /users: Retrieve a list of all users.
# GET /users/<int:user_id>: Retrieve a single user by ID.
# POST /users: Add a new user. The request body should contain username and email.
# PUT /users/<int:user_id>: Update an existing user by ID. The request body should contain username and/or email.
# DELETE /users/<int:user_id>: Delete a user by ID.
# GET /users/<int:user_id>/tasks: Retrieve all tasks associated with a specific user.

users = []

@app.route('/users')
def get_users():
    return jsonify(users)

@app.route('/users/<int:user_id>')
def get_user(user_id):
    for user in users:
        if user.get('id') == user_id:
            return jsonify(user)
    return jsonify(message='User not found'), 404

@app.route('/users', methods=['POST'])
def create_user():
    new_user = request.json
    users.append(new_user)
    return jsonify(new_user), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def replace_user(user_id):
    new_user = request.json
    for user in users:
        if user.get('id') == user_id:
            user.update(new_user)
            return jsonify(new_user)
    return jsonify(message='User not found'), 404

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    initial_length = len(users)
    users = [user for user in users if user.get('id') != user_id]
    if len(users) == initial_length:
        return jsonify(message='User not found'), 404
    return jsonify(message='User deleted successfully'), 204


if __name__ == '__main__':
    app.run(debug=True)

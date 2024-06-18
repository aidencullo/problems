from flask import Flask, jsonify, request

app = Flask(__name__)

 
users = []
tasks = []
user_id_counter = 1
task_id_counter = 1

@app.route('/users')
def get_users():
    return jsonify(users)

@app.route('/users/<int:user_id>')
def get_user(user_id):
    for user in users:
        if user.get('id') == user_id:
            return jsonify(user)
    return jsonify(message='User not found'), 404

@app.route('/users/<int:user_id>/tasks')
def get_tasks_by_user(user_id):
    return jsonify([
        task
        for task in tasks
        if task.get('user_id') == user_id
    ])

@app.route('/users', methods=['POST'])
def create_user():
    global user_id_counter
    new_user = request.json
    new_user.update({'id': user_id_counter})
    user_id_counter += 1
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
    global tasks
    initial_users = len(users)
    initial_tasks = len(tasks)
    users = [user for user in users if user.get('id') != user_id]
    tasks = [task for task in tasks if task.get('user_id') != user_id]
    
    if len(users) == initial_users:
        return jsonify(message='User not found'), 404
    return jsonify(message='User deleted successfully'), 204



@app.route('/tasks')
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks/<int:task_id>')
def get_task(task_id):
    for task in tasks:
        if task.get('id') == task_id:
            return jsonify(task)
    return jsonify(message='Task not found'), 404

@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_counter
    new_task = request.json
    new_task.update({'id': task_id_counter})
    task_id_counter += 1
    tasks.append(new_task)
    return jsonify(new_task), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def replace_task(task_id):
    new_task = request.json
    for task in tasks:
        if task.get('id') == task_id:
            task.update(new_task)
            return jsonify(new_task)
    return jsonify(message='Task not found'), 404

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    initial_length = len(tasks)
    tasks = [task for task in tasks if task.get('id') != task_id]
    if len(tasks) == initial_length:
        return jsonify(message='Task not found'), 404
    return jsonify(message='Task deleted successfully'), 204


if __name__ == '__main__':
    app.run(debug=True)

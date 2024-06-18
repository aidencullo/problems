from flask import Flask, jsonify, request, abort

app = Flask(__name__)


users = []
tasks = []
user_id_counter = 1
task_id_counter = 1


def get_user_by_id(user_id):
    return next((user for user in users if user['id'] == user_id), None)


def remove_user_tasks(user_id):
    global tasks
    tasks = [task for task in tasks if task['user_id'] != user_id]


def get_task_by_id(task_id):
    return next((task for task in tasks if task['id'] == task_id), None)


@app.route('/users')
def get_all_users():
    return jsonify(users), 200


@app.route('/users/<int:user_id>')
def get_user(user_id):
    user = get_user_by_id(user_id)
    if not user:
        abort(404, f"User with ID {user_id} not found")
    return jsonify(user), 200


@app.route('/users/<int:user_id>/tasks')
def get_tasks_by_user(user_id):
    return jsonify([
        task
        for task in tasks
        if task['user_id'] == user_id
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
    user = get_user_by_id(user_id)
    if not user:
        abort(404, f"User with ID {user_id} not found")

    new_user = request.json
    user.update(new_user)
    return jsonify(new_user)


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = get_user_by_id(user_id)
    if not user:
        abort(404, f"User with ID {user_id} not found")

    users.remove(user)
    remove_user_tasks(user_id)
    return '', 204


@app.route('/tasks')
def get_all_tasks():
    return jsonify(tasks)


@app.route('/tasks/<int:task_id>')
def get_task(task_id):
    task = get_task_by_id(task_id)
    if not task:
        abort(404, f"Task with ID {task_id} not found")
    return jsonify(task)


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
    task = get_task_by_id(task_id)
    if not task:
        abort(404, f"Task with ID {task_id} not found")

    new_task = request.json
    task.update(new_task)
    return jsonify(new_task)


@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    initial_length = len(tasks)
    tasks = [task for task in tasks if task.get('id') != task_id]
    if len(tasks) == initial_length:
        abort(404, f"Task with ID {task_id} not found")
    return jsonify(message='Task deleted successfully'), 204


if __name__ == '__main__':
    app.run(debug=True)

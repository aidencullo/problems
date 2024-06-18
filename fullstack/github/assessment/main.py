import json
import traceback
import flask

from save import save


app = flask.Flask(__name__)


def create_user(data):
    if 'name'  not in data:
        return None
    if 'age' not in data:
        return None
    if len(data['name']) > 32:
        return None
    if not isinstance(data['age'], int):
        return None
    if data['age'] < 16:
        return None
    return data


@app.route("/users", methods=["POST"])
def users():

    print("Request received")
    json_str = request.data.decode('utf-8')  # Assuming JSON data is sent as bytes
    # data = flask.request.json
    data = json.loads(json_str)

    user = create_user(data)
    if user is None:
        return flask.jsonify({"error": "invalid user data"}), 400
    save(user)
    return flask.jsonify(user), 201

if __name__ == "__main__":
    app.run()

from flask import Flask
app = Flask(__name__)
from flask import Flask, jsonify
from flask import request
import json

todos = [
    { "label": "My first task", "done": True },
    { "label": "My second task", "done": True }
]

@app.route('/todos', methods=['GET'])
def get_todos():
    json_text = jsonify(todos)
    return json_text, 200




@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    decoded_object = json.loads (request_body)
    return jsonify(decoded_object), 200

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    print("This is the position to delete: ",position)
    return jsonify(todos), 200











if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
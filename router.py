from python_app import handler
from flask import Flask, request, jsonify, abort
from flask_jsontools import DynamicJSONEncoder
import logging

app = Flask("Python app")
app.json_encoder = DynamicJSONEncoder


@app.route('/')
def get_all_todos():
    logger = logging.getLogger(__name__)
    logger.info("Get all to-dos incomming request")
    todos = handler.get_todos()
    if todos is None:
        abort(404)
    return jsonify(todos)


@app.route('/<todo_id>')
def get_todo(todo_id):
    logger = logging.getLogger(__name__)
    logger.info("Get to-do incomming request")
    todo = handler.get_todo(todo_id)
    if todo is None:
        abort(404)
    return jsonify(todo)


@app.route('/<todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    logger = logging.getLogger(__name__)
    logger.info("Delete to-do incomming request")
    result = handler.delete_todo(todo_id)
    if result is None:
        return abort(404)
    return "OK"


@app.route('/', methods=['POST'])
def add_todo():
    logger = logging.getLogger(__name__)
    logger.info("Add to-do incomming request")
    todo_description = request.form.get('todo')
    todo_id = request.form.get('id')
    return handler.add_todo(todo_id, todo_description)


@app.route('/<todo_id>', methods=['PUT'])
def update_todo(todo_id):
    logger = logging.getLogger(__name__)
    logger.info("Update to-do incomming request")
    todo_description = request.form.get('todo')
    return handler.update_todo(todo_id, todo_description)

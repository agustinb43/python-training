from python_app import handler
from flask import Flask, request, jsonify
import logging

app = Flask("Python app")

@app.route('/')
def get_all_todos():
    logger = logging.getLogger(__name__)
    logger.info("Get all to-dos incomming request")
    return jsonify(handler.get_todos())

@app.route('/<todo_id>')
def get_todo(todo_id):
    logger = logging.getLogger(__name__)
    logger.info("Get to-do incomming request")
    return jsonify(handler.get_todo(todo_id))

@app.route('/<todo_id>', methods = ['DELETE'])
def delete_todo(todo_id):
    logger = logging.getLogger(__name__)
    logger.info("Delete to-do incomming request")
    return handler.delete_todo(todo_id)

@app.route('/', methods = ['POST'])
def add_todo():
    logger = logging.getLogger(__name__)
    logger.info("Add to-do incomming request")
    todo_description = request.form.get('todo')
    todo_id = request.form.get('id')
    return handler.add_todo(todo_id, todo_description)

@app.route('/<todo_id>', methods = ['PUT'])
def update_todo(todo_id):
    logger = logging.getLogger(__name__)
    logger.info("Update to-do incomming request")
    todo_description = request.form.get('todo')
    return handler.update_todo(todo_id, todo_description)
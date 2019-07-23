from python_app import handler
from flask import Flask, request

app = Flask("Python app")

@app.route('/')
def get_all_todos():
    return handler.get_todos()

@app.route('/<todo_id>')
def get_todo(todo_id):
    return handler.get_todo(todo_id)

@app.route('/<todo_id>', methods = ['DELETE'])
def delete_todo(todo_id):
    return handler.delete_todo(todo_id)

@app.route('/', methods = ['POST'])
def add_todo():
    todo_description = request.form.get('todo')
    todo_id = request.form.get('id')
    return handler.add_todo(todo_id, todo_description)

@app.route('/<todo_id>', methods = ['PUT'])
def update_todo(todo_id):
    todo_description = request.form.get('todo')
    return handler.update_todo(todo_id, todo_description)
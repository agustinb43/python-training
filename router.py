from python_app import controller
from flask import Flask, request

app = Flask("Python app")

@app.route('/')
def get_todos():
    return controller.get_todos()

@app.route('/', methods = ['POST'])
def add_todo():
    todo = request.form.get('todo')
    return controller.add_todo(todo)
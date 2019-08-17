from python_app.repository import Repository
from python_app.todo import Todo
import sqlite3
import logging
from sqlalchemy.orm.exc import NoResultFound


def get_todos():
    logger = logging.getLogger(__name__)
    repository = Repository()
    logger.info("Finding all to-dos")
    with repository as session:
        return session.query(Todo).all()


def get_todo(todo_id):
    logger = logging.getLogger(__name__)
    repository = Repository()
    logger.info("Finding todo with id %s", todo_id)
    with repository as session:
        try:
            return session.query(Todo).filter(Todo.id == todo_id).one()
        except NoResultFound:
            return None


def add_todo(todo_id, todo_description):
    logger = logging.getLogger(__name__)
    repository = Repository()
    logger.info("Adding new TODO %s:%s", todo_id, todo_description)
    with repository as session:
        logger.info("Adding new to-do")
        todo = Todo(todo_id, todo_description)
        session.add(todo)
        session.commit()
    return "Todo {0} saved".format(todo_id)


def delete_todo(todo_id):
    logger = logging.getLogger(__name__)
    repository = Repository()
    logger.info("Delete todo with id %s", todo_id)
    with repository as session:
        todo = session.query(Todo).get(todo_id)
        if todo is None:
            return None
        else:
            session.delete(todo)
            session.commit()
            return "Todo {0} deleted".format(todo_id)


def update_todo(todo_id, todo_description):
    logger = logging.getLogger(__name__)
    repository = Repository()
    logger.info("Update TODO %s", todo_id)
    with repository as session:
        logger.info("Finding to-do")
        todo = session.query(Todo).get(todo_id)
        if(todo is None):
            logger.info("To-do with id %s not founded", todo_id)
            return none
        logger.info("Updating to-do")
        todo.description = todo_description
        session.commit()
        result = "Todo {0} Updated".format(todo_id)
    return result

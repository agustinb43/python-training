from python_app.repository import Repository
import sqlite3
import logging

def get_todos():
    logger = logging.getLogger(__name__)
    repository = Repository()
    logger.info("Finding all to-dos")
    with repository as db:
        rows = db.cursor().execute('''SELECT id, todo FROM todos''').fetchall()
        all_rows = [{'id':row[0],'todo':row[1]} for row in rows]
    return all_rows

def get_todo(todo_id):
    logger = logging.getLogger(__name__)
    repository = Repository()
    logger.info("Finding todo with id %s", todo_id)
    with repository as db:
        row = db.cursor().execute('''SELECT id, todo FROM todos where id = ? ''', (todo_id)).fetchone()
        if row is not None:
            row = {'id':row[0],'todo':row[1]}
    return row

def delete_todo(todo_id):
    logger = logging.getLogger(__name__)
    repository = Repository()
    logger.info("Delete todo with id %s", todo_id)
    with repository as db:
        db.cursor().execute('''DELETE FROM todos where id = ? ''', (todo_id))
        db.commit()
    return "Todo {0} deleted".format(todo_id)

def add_todo(todo_id, todo_description):
    logger = logging.getLogger(__name__)
    repository = Repository()
    logger.info("Adding new TODO %s:%s", todo_id, todo_description)
    with repository as db:
        logger.info("Adding new to-do")
        db.cursor().execute('''INSERT INTO todos(id, todo) VALUES(:id , :todo)''', {'id':todo_id ,'todo':todo_description})
        db.commit()
    return "Todo {0} saved".format(todo_id)

def update_todo(todo_id, todo_description):
    logger = logging.getLogger(__name__)
    repository = Repository()
    logger.info("Update TODO %s", todo_id)
    with repository as db:
        logger.info("Finding to-do")
        row = db.cursor().execute('''SELECT id, todo FROM todos where id = ? ''', (todo_id)).fetchone()
        if(row is None):
            logger.info("To-do with id %s not founded", todo_id)
            result = "To-do with id {0} not founded".format(todo_id)
        else:
            logger.info("Updating to-do")
            db.cursor().execute('''UPDATE todos SET todo = :todo WHERE id = :id''', {'id':todo_id ,'todo':todo_description})
            db.commit()
            result = "Todo {0} Updated".format(todo_id)
    return result
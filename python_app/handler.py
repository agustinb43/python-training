from python_app.repository import Repository
import sqlite3

class Handler(object):
    """TO-DO Handler"""

    repository = Repository()

    def get_todos(self):
        print("Finding todos")
        with self.repository as db:
            db.row_factory = sqlite3.Row
            rows = db.cursor().execute('''SELECT id, todo FROM todos''')
            result = "TO-DOS: \n"
            for row in rows:
                result += "{0} : {1} \n".format(row['id'], row['todo'])
        return result

    def get_todo(self, todo_id):
        print("Finding todo with id {0}".format(todo_id))
        with self.repository as db:
            row = db.cursor().execute('''SELECT id, todo FROM todos where id = ? ''', (todo_id)).fetchone()
        result = "TO-DO: \n "
        if(row is None):
            print("To-do with id {0} not founded".format(todo_id))
            result += "To-do with id {0} not founded".format(todo_id)
        else:
            result += "{0} : {1}".format(row[0], row[1])
        return result

    def delete_todo(self, todo_id):
        print("Delete todo with id {0}".format(todo_id))
        with self.repository as db:
            db.cursor().execute('''DELETE FROM todos where id = ? ''', (todo_id))
            db.commit()
        return "Todo {0} deleted".format(todo_id)

    def add_todo(self, todo_id, todo_description):
        print("Adding new TODO {0}:{1}".format(todo_id, todo_description))
        with self.repository as db:
            print("Adding new to-do")
            db.cursor().execute('''INSERT INTO todos(id, todo) VALUES(:id , :todo)''', {'id':todo_id ,'todo':todo_description})
            db.commit()
        return "Todo {0} saved".format(todo_id)

    def update_todo(self, todo_id, todo_description):
        print("Update TODO {0}".format(todo_id))
        with self.repository as db:
            print("Finding to-do")
            row = db.cursor().execute('''SELECT id, todo FROM todos where id = ? ''', (todo_id)).fetchone()
            if(row is None):
                print("To-do with id {0} not founded".format(todo_id))
                result = "To-do with id {0} not founded".format(todo_id)
            else:
                print("Updating to-do")
                db.cursor().execute('''UPDATE todos SET todo = :todo WHERE id = :id''', {'id':todo_id ,'todo':todo_description})
                db.commit()
                result = "Todo {0} Updated".format(todo_id)
        return result
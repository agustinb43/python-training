import sqlite3

class Service(object):
    """To-do list service"""
    
    def __init__(self): 
        # Create a database in RAM
        print("Starting DB")
        self.db = sqlite3.connect(':memory:', check_same_thread=False)
        self.cursor = self.db.cursor()
        self.cursor.execute('''CREATE TABLE todos(id INTEGER PRIMARY KEY, todo TEXT)''')
        self.db.commit()
        print("DB OK")

    def add_todo(self, new_todo):
        print("Adding new to-do")
        self.cursor.execute('''INSERT INTO todos(todo)
                  VALUES(:todo)''',
                  {'todo':new_todo})
        self.db.commit()

    def list_todos(self):
        print("Finding todos")
        self.cursor.execute('''SELECT todo FROM todos''')
        all_rows = self.cursor.fetchall()
        return all_rows

    def __del__(self):
        self.db.close()
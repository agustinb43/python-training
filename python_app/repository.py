import sqlite3

class Repository():
    """ SQLlite3 repository """
    def startup(self):
         # Create a database in RAM
        print("Starting DB")
        self.db = sqlite3.connect('test.db')
        self.db.cursor().execute('''CREATE TABLE IF NOT EXISTS todos(id INTEGER PRIMARY KEY, todo TEXT)''')
        self.db.commit()
        self.db.close()
        print("DB created OK")

    def __enter__(self):
        print("Getting db connection")
        self.db = sqlite3.connect('test.db')
        return self.db

    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing db connection")
        self.db.close()
        return False
    
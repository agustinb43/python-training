import sqlite3

def startup():
    # Create a database
    db = sqlite3.connect('test.db')
    db.cursor().execute('''CREATE TABLE IF NOT EXISTS todos(id INTEGER PRIMARY KEY, todo TEXT)''')
    db.commit()
    db.close()
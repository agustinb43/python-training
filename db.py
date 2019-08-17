import sqlite3

def startup():
    # Create a database
    db = sqlite3.connect('test.db')
    db.cursor().execute('''CREATE TABLE IF NOT EXISTS todos(id INTEGER PRIMARY KEY, description TEXT)''')
    db.commit()
    # db.cursor().execute('''INSERT INTO todos (id, description) VALUES ('1', 'aaaaaaaa')''')
    # db.commit()
    db.close()
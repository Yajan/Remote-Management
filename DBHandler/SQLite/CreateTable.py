import sqlite3
db = sqlite3.connect('Data/test.db')
c = db.cursor()
c.execute('''CREATE TABLE test(id INTEGER PRIMARY KEY,INTEGER  data, script TEXT)''')
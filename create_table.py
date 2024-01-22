import sqlite3

connection = sqlite3.connect('data.db')

connection.execute('''
CREATE TABLE users(
id INTEGER  PRIMARY KEY,
name VARCHAR(255),
username VARCHAR(255),
password INTEGER
)

''')

connection.commit()
connection.close()

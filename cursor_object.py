import sqlite3

connection = sqlite3.connect('data.db')

connection.commit()
connection.close()


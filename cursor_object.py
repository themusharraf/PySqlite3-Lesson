import sqlite3

connection = sqlite3.connect('data.db')

connection.commit()  # Commit changes to database
connection.close()  # Closing the connection

import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.execute("SELECT * FROM users")

for row in cursor:
    print(row)

connection.commit()
connection.close()

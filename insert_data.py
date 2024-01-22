import sqlite3

connection = sqlite3.connect('data.db')

connection.execute("INSERT INTO users VALUES (1, 'John','john',1234 )")
connection.execute("INSERT INTO users VALUES (2,'Ali','ali',2222 )")
connection.execute("INSERT INTO users VALUES (3,'Bekzod','bek',4444 )")

connection.commit()
connection.close()

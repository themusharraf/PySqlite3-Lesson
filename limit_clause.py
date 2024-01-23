import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.execute("SELECT * FROM customer_address LIMIT 4")


for x in cursor:
    print(x)

connection.commit()
connection.close()


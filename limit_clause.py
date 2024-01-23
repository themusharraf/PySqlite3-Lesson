import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.execute("SELECT * FROM customer_address LIMIT 3")


for i in cursor:
    print(i)

connection.commit()
connection.close()


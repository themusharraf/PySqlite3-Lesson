import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.execute("SELECT * FROM users")

for row in cursor:
    print(row)
# output
""" 
(1, 'John', 'john', 1234)
(2, 'Ali', 'ali', 2222)
(3, 'Bekzod', 'bek', 4444)
"""

connection.commit()
connection.close()

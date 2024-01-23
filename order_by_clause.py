import sqlite3

connection = sqlite3.connect('data.db')
# create table
# connection.execute('''CREATE TABLE customer_address
#          (ID INT PRIMARY KEY     NOT NULL,
#          NAME           TEXT    NOT NULL,
#          AGE            INT     NOT NULL,
#          ADDRESS        CHAR(50)); ''')



connection.commit()
connection.close()

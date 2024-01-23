import sqlite3

connection = sqlite3.connect('data.db')
# create table
# connection.execute('''CREATE TABLE customer_address
#          (ID INT PRIMARY KEY     NOT NULL,
#          NAME           TEXT    NOT NULL,
#          AGE            INT     NOT NULL,
#          ADDRESS        CHAR(50)); ''')
# -------------------------------------------------------------

# insert data table

# connection.execute(
#     "INSERT INTO customer_address VALUES (1, 'nikhil teja', 22, 'hyderabad' )")
# connection.execute(
#     "INSERT INTO customer_address VALUES (2, 'karthik', 25, 'khammam')")
# connection.execute(
#     "INSERT INTO customer_address VALUES (3, 'sravan', 22, 'ponnur' )")
# connection.execute(
#     "INSERT INTO customer_address VALUES (4, 'deepika', 25, 'chebrolu' )")
# connection.execute(
#     "INSERT INTO customer_address VALUES (5, 'jyothika', 22, 'noida')")
# -------------------------------------------------------------

# cursor = connection.execute(
#     "SELECT ADDRESS,ID from customer_address ORDER BY address DESC")
#
# for x in cursor:
#     print(x)

# -------------------------------------------------------------

# cursor = connection.execute(
#     "SELECT NAME,ID from customer_address ORDER BY NAME DESC")
#
# # display data row by row
# for i in cursor:
#     print(i)

# -------------------------------------------------------------



connection.commit()
connection.close()

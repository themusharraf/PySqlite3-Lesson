import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# create table
cursor.execute("DROP TABLE IF EXISTS Student")
createTable = '''CREATE TABLE Student( 
   Student_ID int,
   First_Name VARCHAR(100), 
   Last_Name VARCHAR(100),
   Age int, 
   Department VARCHAR(100) 
)'''
cursor.execute(createTable)

# check the database creation data
if cursor:
    print("Database Created Successfully !")
else:
    print("Database Creation Failed !")

connection.commit()
connection.close()


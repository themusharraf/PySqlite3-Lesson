import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# 1 create table.
# cursor.execute("DROP TABLE IF EXISTS Student")
# createTable = '''CREATE TABLE Student(
#    Student_ID int,
#    First_Name VARCHAR(100),
#    Last_Name VARCHAR(100),
#    Age int,
#    Department VARCHAR(100)
# )'''
# cursor.execute(createTable)

# 2 check the database creation data.
# if cursor:
#     print("Database Created Successfully !")
# else:
#     print("Database Creation Failed !")

# 3 Now we will insert data into Student table.
# Insert data into the table
# cursor.execute("INSERT INTO Student VALUES (1,'Akbar', 'Jalolov', 21, 'IT')")
# cursor.execute("INSERT INTO Student VALUES (2,'Nodir', 'Boburov', 21, 'IT')")
# cursor.execute("INSERT INTO Student VALUES (3,'Jasur', 'Kamolov', 30, 'CIVIL')")
# cursor.execute("INSERT INTO Student VALUES (4,'Rustam', 'Akbarov', 32, 'COMP')")
#
# # printing the cursor data
# if cursor:
#     print("Data Inserted !")
# else:
#     print("Data Insertion Failed !")

# 4 To retrieve the data of the students whose Department is IT
# IT bo'limi bo'lgan talabalarning ma'lumotlarini olish uchun

# WHERE CLAUSE TO RETRIEVE DATA
cursor.execute("SELECT * FROM Student WHERE Department = 'IT'")

# printing the cursor data
print(cursor.fetchall())




connection.commit()
connection.close()


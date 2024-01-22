import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# -------------------------------------------------------------
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

# -------------------------------------------------------------
# 2 check the database creation data.
# if cursor:
#     print("Database Created Successfully !")
# else:
#     print("Database Creation Failed !")

# -------------------------------------------------------------
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

# -------------------------------------------------------------
# 4 To retrieve the data of the students whose Department is IT
# IT bo'limi bo'lgan talabalarning ma'lumotlarini olish uchun

# WHERE CLAUSE TO RETRIEVE DATA
# cursor.execute("SELECT * FROM Student WHERE Department = 'IT'")


# printing the cursor data
# print(cursor.fetchall())
# output [(1, 'Akbar', 'Jalolov', 21, 'IT'), (2, 'Nodir', 'Boburov', 21, 'IT')]

# -------------------------------------------------------------
# 5 To retrieve the data of the students whose First Name starts with ‘R’.
# We can also use Wildcard characters with where clause as shown below
# Ismi "R" bilan boshlanadigan talabalarning ma'lumotlarini olish uchun. # noqa

# cursor.execute("SELECT * from Student WHERE First_name Like'R%'")
#
# print(cursor.fetchall())

# -------------------------------------------------------------
# 6 To update the data of student whose Student ID is 4
# Talaba ID raqami 4 bo'lgan talabaning ma'lumotlarini yangilash # noqa

# where clause to update data
# cursor.execute("UPDATE Student SET Department ='E&TC' WHERE Student_ID = 2")

# printing the cursor data
# cursor.execute("SELECT * from Student")
# print(cursor.fetchall())

# -------------------------------------------------------------
# 7 To Delete the data of student whose Age ID is 30
# Yosh ID raqami 30 bo'lgan talabaning ma'lumotlarini o'chirish # noqa


# where clause to delete data
cursor.execute("DELETE from Student WHERE Age = 32")

cursor.execute("SELECT * from Student")
print(cursor.fetchall())



connection.commit()
connection.close()


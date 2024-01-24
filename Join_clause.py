"""
 JOIN bandi umumiy atributlar asosida ikkita jadvaldagi yozuvlarni birlashtiradi. Har xil turdagi ulanishlar quyidagilar:

INNER JOIN (OR JOIN) - ikkala jadvalda umumiy atributlarga ega bo'lgan yozuvlarni beradi.
LEFT JOIN - chap jadvaldagi barcha yozuvlarni va faqat o'ng jadvaldagi umumiy yozuvlarni beradi.
RIGHT JOIN - o'ng jadvaldagi barcha yozuvlarni va faqat chap jadvaldagi umumiy yozuvlarni beradi.
FULL OUTER JOIN - chap yoki o'ng jadvalda umumiy atribut mavjud bo'lganda barcha yozuvlarni beradi.
CROSS JOIN - bir jadvalning yozuvlarini boshqa jadvalning barcha boshqa yozuvlari bilan birga beradi.

"""  # noqa

import sqlite3

connection = sqlite3.connect('data.db')

# Create cursor object
cursor = connection.cursor()

# Create and populate tables
# cursor.executescript('''
# CREATE TABLE Advisor(
# AdvisorID INTEGER NOT NULL,
# AdvisorName TEXT NOT NULL,
# PRIMARY KEY(AdvisorID)
# );
#
# CREATE TABLE Student(
# StudentID NUMERIC NOT NULL,
# StudentName NUMERIC NOT NULL,
# AdvisorID INTEGER,
# FOREIGN KEY(AdvisorID) REFERENCES Advisor(AdvisorID),
# PRIMARY KEY(StudentID)
# );
#
# INSERT INTO Advisor(AdvisorID, AdvisorName) VALUES
# (1,"John Paul"),
# (2,"Anthony Ali"),
# (3,"Rustam Shokir"),
# (4,"Salim Rustam"),
# (5,"Arthur Clintwood");
#
# INSERT INTO Student(StudentID, StudentName, AdvisorID) VALUES
# (501,"AllNc1",1),
# (502,"AllNc2",1),
# (503,"AllNc3",3),
# (504,"AllNc4",2),
# (505,"AllNc5",4),
# (506,"AllNc6",2),
# (507,"AllNc7",2),
# (508,"AllNc8",3),
# (509,"AllNc9",NULL),
# (510,"AllNc10",1);
#
# ''')

# ---------- INNER JOIN (OR JOIN) - ikkala jadvalda umumiy atributlarga ega bo'lgan yozuvlarni beradi. # noqa
# Query for INNER JOIN
# sql = '''SELECT StudentID, StudentName, AdvisorName  FROM Student  INNER JOIN Advisor ON Student.AdvisorID = Advisor.AdvisorID;'''
#
# # Executing the query
# cursor.execute(sql)
#
# # Fetching rows from the result table # ma'lumotlarni olish # noqa
# result = cursor.fetchall()
# for row in result:
#     print(row)

# ----------LEFT JOIN - chap jadvaldagi barcha yozuvlarni va faqat o'ng jadvaldagi umumiy yozuvlarni beradi. # noqa
# Query for LEFT JOIN
# sql = '''SELECT StudentID, StudentName, AdvisorName  FROM Student  LEFT JOIN Advisor USING(AdvisorID) ;'''
#
# # Executing the query
# cursor.execute(sql)
#
# # Fetching rows from the result table
# result = cursor.fetchall()
# for row in result:
#     print(row)

# ----------RIGHT JOIN - o'ng jadvaldagi barcha yozuvlarni va faqat chap jadvaldagi umumiy yozuvlarni beradi. # noqa
# Query for RIGHT JOIN
# sql = '''SELECT StudentID, StudentName, AdvisorName  FROM Advisor  LEFT JOIN Student USING(AdvisorID);'''
#
# # Executing the query
# cursor.execute(sql)
#
# # Fetching rows from the result table
# result = cursor.fetchall()
# for row in result:
#     print(row)

# ----------FULL OUTER JOIN - chap yoki o'ng jadvalda umumiy atribut mavjud bo'lganda barcha yozuvlarni beradi. # noqa

# Query for FULL OUTER JOIN
# sql = '''SELECT StudentID, StudentName, AdvisorName
# FROM Student
# LEFT JOIN Advisor
# USING(AdvisorID)
# UNION ALL
# SELECT StudentID, StudentName, AdvisorName
# FROM Advisor
# LEFT JOIN Student
# USING(AdvisorID)
# WHERE Student.AdvisorID IS NULL;'''
#
# # Executing the query
# cursor.execute(sql)
#
# # Fetching rows from the result table
# result = cursor.fetchall()
# for row in result:
#     print(row)

# ---------CROSS JOIN - bir jadvalning yozuvlarini boshqa jadvalning barcha boshqa yozuvlari bilan birga beradi.  # noqa
# Query for CROSS JOIN
sql = '''SELECT StudentID, StudentName, AdvisorName  FROM Student  CROSS JOIN Advisor;'''

# Executing the query
cursor.execute(sql)

# Fetching rows from the result table
result = cursor.fetchall()
for row in result:
    print(row)


connection.commit()
connection.close()

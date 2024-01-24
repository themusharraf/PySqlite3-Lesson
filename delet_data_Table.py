import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS ALLNC")

# Creating table
table = """ CREATE TABLE ALLNC (
            Email VARCHAR(255) NOT NULL,
            Name CHAR(25) NOT NULL,
            Score INT
        ); """

cursor.execute(table)

# inserting data into ALLNC table
cursor.execute("""INSERT INTO ALLNC (Email,Name,Score) VALUES ("allnc1@gmail.com","Allnc1",25)""")
cursor.execute("""INSERT INTO ALLNC (Email,Name,Score) VALUES ("allnc2@gmail.com","Allnc2",15)""")
cursor.execute("""INSERT INTO ALLNC (Email,Name,Score) VALUES ("allnc3@gmail.com","Allnc3",36)""")
cursor.execute("""INSERT INTO ALLNC (Email,Name,Score) VALUES ("allnc4@gmail.com","Allnc4",27)""")
cursor.execute("""INSERT INTO ALLNC (Email,Name,Score) VALUES ("allnc5@gmail.com","Allnc5",40)""")
cursor.execute("""INSERT INTO ALLNC (Email,Name,Score) VALUES ("allnc6@gmail.com","Allnc6",14)""")
cursor.execute("""INSERT INTO ALLNC (Email,Name,Score) VALUES ("allnc7@gmail.com","Allnc7",10)""")

connection.commit()  # Commit changes to database
connection.close()  # Closing the connection

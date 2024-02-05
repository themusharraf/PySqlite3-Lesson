import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('preson.db')
cursor = conn.cursor()

# Define the users table if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        full_name TEXT NOT NULL
    )
''')
conn.commit()


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def add_user(self, user_id, full_name):
        with self.connection:
            return self.cursor.execute("INSERT INTO 'users' ('user_id',full_name) VALUES (?,?)", (user_id, full_name))

    def get_all_users(self):
        with self.connection:
            return self.cursor.execute("SELECT user_id, full_name FROM users").fetchall()

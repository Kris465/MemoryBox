import sqlite3


class Database:
    def __init__(self, db_name="database.db"):
        self.db_name = db_name
        self.connection = None

    def connect(self):
        self.connection = sqlite3.connect(self.db_name)
        # Create table if it doesn't exist
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS numbers (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            value INTEGER NOT NULL
                          )''')
        self.connection.commit()
        return self.connection

    def read_from_db(self):
        if not self.connection:
            self.connect()

        cursor = self.connection.cursor()
        cursor.execute("SELECT value FROM numbers ORDER BY id DESC LIMIT 1")
        result = cursor.fetchone()
        return result[0]

    def write_to_db(self, number):
        if not self.connection:
            self.connect()

        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO numbers (value) VALUES (?)", (number,))
        self.connection.commit()

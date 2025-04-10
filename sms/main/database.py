import sqlite3 as sl

# открываем файл с базой данных
con = sl.connect('Grade.db')

with con:
    con.execute("""
        CREATE TABLE Student (
            gender VARCHAR(20) PRIMARY KEY,
            address INTEGER,
            age INTEGER

);
""")

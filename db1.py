import sqlite3


connection = sqlite3.connect('zoo.db')
cursor = connection.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS animals (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name varchar(50) NOT NULL,
                   species varchar(100) NOT NULL,
                   age INTEGER
               )
               ''')

cursor.execute(
    "INSERT INTO animals (name, species, age) VALUES ('лев', 'хищник', 5)")
cursor.execute(
    "INSERT INTO animals (name, species, age) VALUES ('слон', 'млекопитающее', 19)")
cursor.execute(
    "INSERT INTO animals (name, species, age) VALUES ('попугай', 'птица', 2)")

connection.commit()

cursor.execute("SELECT * FROM animals")
rows = cursor.fetchall()

for row in rows:
    print(row)

connection.close()

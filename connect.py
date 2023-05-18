import os
from dotenv import load_dotenv, find_dotenv
import mysql.connector


def connect_db():
    load_dotenv(find_dotenv())
    user = os.environ.get('user')
    password = os.environ.get('password')
    host = os.environ.get('host')
    db = os.environ.get('db')

    cnx = mysql.connector.connect(user=user, password=password,
                                  host=host, database=db)
    cursor = cnx.cursor()

    cursor.execute("SHOW TABLES")

    tables = cursor.fetchall()

    for table in tables:
        print(table)

    cnx.close()


connect_db()

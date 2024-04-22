import psycopg2
from config import *

def Phonebook():
    with connection.cursor() as cursor:
        cursor.execute(
            "CREATE TABLE Phonebook (id BIGINT NOT NULL PRIMARY KEY, User_name VARCHAR(64) NOT NULL, Phone_number BIGINT NOT NULL);"
        )
        print("table created")


try:
    connection = psycopg2.connect(
        host =host,
        user = user,
        password =password,
        database = db_name
    )
    connection.autocommit = True
    

except Exception as _ex:
    print("[INFO] error while working with Postgres", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] Postgres connection closed")
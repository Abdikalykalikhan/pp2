import psycopg2
from config import *

def Phone_book():
    try:
        connection = psycopg2.connect(
            host =host,
            user = user,
            password =password,
            database = db_name
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute(
                "CREATE TABLE Phone_book (id BIGINT NOT NULL PRIMARY KEY, first_name VARCHAR(64) NOT NULL, last_name VARCHAR(64) NOT NULL, Phone_number BIGINT NOT NULL);"
            )
            print("table created")

    except Exception as _ex:
        print("[INFO] error while working with Postgres", _ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] Postgres connection closed")
Phone_book()
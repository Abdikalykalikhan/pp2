import psycopg2
from config import *

def add_entry(id, user_name, phone_number):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO Phonebook (id, User_name, Phone_number) VALUES (%s, %s, %s)",
                (id, user_name, phone_number)
            )
            print("Entry added successfully")

    except Exception as _ex:
        print("[INFO] Error while working with Postgres:", _ex)

    finally:
        if connection:
            connection.close()
            print("[INFO] Postgres connection closed")

# Usage
add_entry(500570, 'Alikhan', 87473939665)
add_entry(500976, 'Temirkhan', 87082346583)
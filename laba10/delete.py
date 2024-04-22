import psycopg2
from config import *

def add_entry(id, User_name, Phone_number):
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
                (id, User_name, Phone_number)
            )
            print("Entry added successfully")

    except Exception as ex:
        print("[INFO] Error while working with Postgres:", ex)

    finally:
        if connection:
            connection.close()
            print("[INFO] Postgres connection closed")

def delete_entry(id, User_name, Phone_number):
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
                "DELETE FROM Phonebook WHERE id = %s",
                (id,)
            )
            cursor.execute(
                "DELETE FROM Phonebook WHERE User_name = %s",
                (User_name,)
            )
            cursor.execute(
                "DELETE FROM Phonebook WHERE Phone_number = %s",
                (Phone_number,)
            )
            print("Entry deleted successfully")

    except Exception as ex:
        print("[INFO] Error while working with Postgres:", ex)

    finally:
        if connection:
            connection.close()
            print("[INFO] Postgres connection closed")


delete_entry(8878956, 'Alikhan', '99999999887' )

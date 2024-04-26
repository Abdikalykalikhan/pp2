import psycopg2
from config import *

def delete_data_by_username_or_phone(username=None, phone=None):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            if username:
                cursor.execute("DELETE FROM Phone_book WHERE first_name = %s OR last_name = %s", (username, username))
            if phone:
                cursor.execute("DELETE FROM Phone_book WHERE phone_number = %s", (phone,))

        print("Data deleted successfully!")

    except Exception as ex:
        print("Error:", ex)

    finally:
        if connection:
            connection.close()

# Example usage:
username = input("Enter username to delete (or leave blank): ")
phone = input("Enter phone number to delete (or leave blank): ")

delete_data_by_username_or_phone(username, phone)


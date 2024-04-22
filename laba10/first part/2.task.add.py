import csv
import psycopg2
from config import *

def insert_data_from_csv():
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            with open("data.csv", mode='r', newline='') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    cursor.execute("""
                        INSERT INTO Phonebook (user_name, id, phone_number)
                        VALUES (%s, %s, %s)
                    """, (row[0], row[1], row[2]))
            print("Data inserted from CSV ")

    except Exception as ex:
        print("[INFO] Error while inserting data:", ex)

    finally:
        if connection:
            connection.close()
            print("[INFO] Postgres connection closed")


def insert_data_from_console():
    user_name = input("Enter name: ")
    id = int(input("Enter id: "))
    phone_number = int(input("Enter phone number: "))
    
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO Phonebook (user_name, id, phone_number)
                VALUES (%s, %s, %s)
            """, (user_name, id, phone_number))
            
        print("Data inserted from console")

    except Exception as ex:
        print("[INFO] Error while inserting data from console:", ex)

    finally:
        if connection:
            connection.close()
            print("[INFO] Postgres connection closed")

insert_data_from_csv() 
insert_data_from_console()
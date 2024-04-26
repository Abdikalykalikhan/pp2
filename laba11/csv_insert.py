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
                        INSERT INTO Phone_book (id, first_name, last_name, phone_number)
                        VALUES (%s, %s, %s, %s)
                    """, (row[0], row[1], row[2], row[3]))
            print("Data inserted from CSV ")

    except Exception as ex:
        print("[INFO] Error while inserting data:", ex)

    finally:
        if connection:
            connection.close()
            print("[INFO] Postgres connection closed")


insert_data_from_csv() 
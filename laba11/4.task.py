import psycopg2
from config import *

def fetch_data_with_pagination(limit, offset):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM {} LIMIT %s OFFSET %s'.format('Phone_book'), (limit, offset))
            rows = cursor.fetchall()

            for row in rows:
                print(row)

    except Exception as ex:
        print("Errrror:", ex)

    finally:
        if connection:
            connection.close()


limit = 10  # Количество записей на странице
offset = 5 # Смещение

fetch_data_with_pagination(limit, offset)

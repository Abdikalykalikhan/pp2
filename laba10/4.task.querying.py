import psycopg2
from config import *

def get_Phonebook():
    """ Retrieve data from the vendors table """

    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute("SELECT id, user_name FROM Phonebook ORDER BY user_name")
            print("The number of parts: ", cursor.rowcount)
            row = cursor.fetchone()

            while row is not None:
                print(row)
                row = cursor.fetchone()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == '__main__':
    get_Phonebook()        
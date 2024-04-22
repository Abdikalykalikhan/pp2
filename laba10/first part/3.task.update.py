import psycopg2
from config import *


def update_Phonebook(id, user_name):
    """ Update Phonebook name based on the Phonebook id """
       
    updated_row_count = 0

    sql = """ UPDATE Phonebook
                SET user_name = %s
                WHERE id = %s"""
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        connection.autocommit = True 
        with  connection.cursor() as cursor:
            cursor.execute(sql, (user_name, id))
            updated_row_count = cursor.rowcount    

        connection.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    finally:
        return updated_row_count

if __name__ == '__main__':
    update_Phonebook(500570, "Ismail")
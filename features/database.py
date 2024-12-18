from features.config import get_db_connection
import mysql.connector

def execute_query(query, params=None):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(query, params)
        connection.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()

def fetch_query(query, params=None):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    result = None
    try:
        cursor.execute(query, params)
        result = cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()
    return result

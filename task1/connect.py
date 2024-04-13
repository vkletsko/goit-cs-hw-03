import psycopg2
from contextlib import contextmanager


@contextmanager
def create_connection():
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="hw03",
            user="postgres",
            password="567234",
            port="5432",
        )
        try:
            yield connection
        finally:
            connection.close()
    except psycopg2.OperationalError as e:
        print(f"Connection failed. Error: {e}")
        return None
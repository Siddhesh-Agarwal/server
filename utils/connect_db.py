import psycopg2
import os


def connect_db():
    """Function to create and return database connection and cursor."""
    dbname = os.environ["DB_NAME"]
    user = os.environ["DB_USER"]
    host = os.environ["DB_HOST"]
    password = os.environ["DB_PASSWORD"]

    conn_str = f"dbname='{dbname}' user='{user}' host='{host}' password='{password}'"
    conn = psycopg2.connect(conn_str)
    cur = conn.cursor()
    return conn, cur

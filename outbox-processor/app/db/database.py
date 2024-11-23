import psycopg2
from datetime import datetime

conn = psycopg2.connect(
    dbname="orderdb",
    user="user",
    password="password",
    host="db",
    port="5432"
)


def fetch_waiting():
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM outbox WHERE status = 'waiting'")
        result = cursor.fetchall()
        cursor.execute("UPDATE outbox SET status = 'execution' WHERE status = 'waiting'")
        conn.commit()
        return result


def success_on_cancel(id):
    with conn.cursor() as cursor:
        cursor.execute(f"DELETE FROM outbox WHERE id = {id}")
        conn.commit()


def error_on_cancel(id):
    with conn.cursor() as cursor:
        cursor.execute(f"UPDATE outbox SET status = 'waiting' WHERE id = {id}")
        conn.commit()


import logging

logging.basicConfig(level=logging.DEBUG)

def get_tables():
    with conn.cursor() as cursor:
        cursor.execute(f"SELECT * FROM outbox")
        result = cursor.fetchall()
        print("outbox:\n\n")
        logging.debug(result)
        cursor.execute(f"SELECT * FROM orders")
        result = cursor.fetchall()
        print("orders:\n\n")
        logging.debug(result)
        conn.commit()

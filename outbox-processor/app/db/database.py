import psycopg2
from datetime import datetime

conn = psycopg2.connect(
    dbname="orderdb",
    user="user",
    password="jeusf23aco3oa9a9a0",
    host="db-data",
    port="5432"
)


def create_outbox():
    with conn.cursor() as cursor:
        cursor.execute("SELECT 1 FROM pg_type WHERE typname = 'status'")
        result = cursor.fetchone()
        if not result:
            cursor.execute("CREATE TYPE status AS ENUM ('waiting', 'execution')")
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS outbox (
            id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            payload JSON,
            status status
        )
        """)
        conn.commit()


def drop_db():
    with conn.cursor() as cursor:
        cursor.execute("DROP TABLE IF EXISTS orders CASCADE")
        cursor.execute("DROP TABLE IF EXISTS outbox CASCADE")
        conn.commit()


def create_partition(name, begin_ts, end_ts):
    index_name = f"index_{name}"
    with conn.cursor() as cursor:
        cursor.execute(f"""
        CREATE TABLE {name} PARTITION OF orders
        FOR VALUES FROM ('{begin_ts}') TO ('{end_ts}')
        """)
        cursor.execute(f"""
        CREATE INDEX {index_name} ON {name} (order_id, assign_time DESC)
        """)
        conn.commit()


def init_db(pt_name, begin_ts, end_ts):
    with conn.cursor() as cursor:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            assign_order_id TEXT,
            order_id TEXT NOT NULL,
            executer_id TEXT,
            base_coin_amount FLOAT,
            coin_coef FLOAT,
            bonus_amount FLOAT,
            final_coin_amount FLOAT,
            route_information TEXT,
            assign_time TIMESTAMP,
            acquire_time TIMESTAMP,
            is_canceled BOOLEAN
        ) PARTITION BY RANGE (assign_time)
        """)
        conn.commit()
    create_partition(pt_name, begin_ts, end_ts)


def drop_index(index_name):
    with conn.cursor() as cursor:
        cursor.execute(f"DROP INXED IF EXISTS {index_name}")


def fetch_waiting():
    with conn.cursor() as cursor:
        cursor.execute("""
        UPDATE outbox
        SET status = 'execution'
        WHERE id IN (
            SELECT id FROM outbox WHERE status = 'waiting' LIMIT 10
        )
        RETURNING *               
        """)
        result = cursor.fetchall()
        return result


def success_on_cancel(ids):
    with conn.cursor() as cursor:
        cursor.execute(f"DELETE FROM outbox WHERE id = ANY(%s)", (ids,))
        conn.commit()


def error_on_cancel():
    with conn.cursor() as cursor:
        conn.rollback()


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

import psycopg2
from datetime import datetime
from model import AssignedOrder

conn = psycopg2.connect(
    dbname="orderdb",
    user="user",
    password="password",
    host="db",
    port="5432"
)

def init_db():
    with conn.cursor() as cursor:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            order_id TEXT PRIMARY KEY,
            assign_time TIMESTAMP,
            acquire_time TIMESTAMP,
            executer_id TEXT,
            zone_display_name TEXT,
            coin_coeff FLOAT,
            bonus_amount FLOAT,
            final_coin_amount FLOAT,
            route_information TEXT
        )
        """)
        conn.commit()

def save_order_to_db(order):
    with conn.cursor() as cursor:
        cursor.execute("""
        INSERT INTO orders (order_id, assign_time, acquire_time, executer_id, zone_display_name, coin_coeff, bonus_amount, final_coin_amount, route_information)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (order_id) DO UPDATE
        SET acquire_time = EXCLUDED.acquire_time
        """, (
            order.order_id, order.assign_time, order.acquire_time, order.executer_id,
            order.route_information, order.coin_coeff, order.bonus_amount, order.final_coin_amount, order.route_information
        ))
        conn.commit()

def get_order_from_db(order_id):
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM orders WHERE order_id = %s", (order_id,))
        row = cursor.fetchone()
        if row:
            return AssignedOrder(*row)
        return None

def delete_order_from_db(order_id):
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM orders WHERE order_id = %s", (order_id,))
        conn.commit()

def get_latest_order_id_for_executer(executer_id):
    with conn.cursor() as cursor:
        cursor.execute("SELECT order_id FROM orders WHERE executer_id = %s ORDER BY assign_time DESC LIMIT 1", (executer_id,))
        row = cursor.fetchone()
        return row[0] if row else None

def close_db():
    conn.close()

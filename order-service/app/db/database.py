import psycopg2
from datetime import datetime
from models.model import AssignedOrder

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
            assign_order_id TEXT PRIMARY KEY,
            order_id TEXT NOT NULL,
            executer_id TEXT,
            coin_coeff FLOAT,
            bonus_amount FLOAT,
            final_coin_amount FLOAT,
            route_information TEXT,
            assign_time TIMESTAMP,
            acquire_time TIMESTAMP
        )
        """)
        conn.commit()

def save_order_to_db(order):
    with conn.cursor() as cursor:
        cursor.execute("""
        INSERT INTO orders (assign_order_id, order_id, executer_id, coin_coeff, bonus_amount, final_coin_amount, route_information, assign_time, acquire_time)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (assign_order_id) DO UPDATE
        SET acquire_time = EXCLUDED.acquire_time
        """, (
            order.assign_order_id,
            order.order_id,
            order.executer_id,
            order.coin_coeff,
            order.coin_bonus_amount,
            order.final_coin_amount,
            order.route_information,
            order.assign_time,
            order.acquire_time
        ))
        conn.commit()


def get_order_from_db(order_id):
    with conn.cursor() as cursor:
        cursor.execute("""
        SELECT assign_order_id, order_id, executer_id, coin_coeff, bonus_amount, final_coin_amount, route_information, assign_time, acquire_time 
        FROM orders WHERE order_id = %s
        """, (order_id,))

        row = cursor.fetchone()
        if row:
            return AssignedOrder(
                assign_order_id=row[0],
                order_id=row[1],
                executer_id=row[2],
                coin_coeff=row[3],
                coin_bonus_amount=row[4],
                final_coin_amount=row[5],
                route_information=row[6],
                assign_time=row[7],
                acquire_time=row[8]
            )
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

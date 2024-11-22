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


def drop_db():
    with conn.cursor() as cursor:
        cursor.execute("DROP TABLE IF EXISTS orders CASCADE")
        conn.commit()


def check_db():
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM information_schema.columns WHERE table_name='orders'")
        columns = cursor.fetchall()
        print(columns)


def init_db():
    with conn.cursor() as cursor:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            assign_order_id TEXT PRIMARY KEY,
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
        )
        """)
        conn.commit()


def save_order_to_db(order):
    with conn.cursor() as cursor:
        cursor.execute("""
        INSERT INTO orders (assign_order_id, order_id, executer_id, base_coin_amount, coin_coef, bonus_amount, final_coin_amount, route_information, assign_time, acquire_time, is_canceled)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            order.assign_order_id,
            order.order_id,
            order.executer_id,
            order.base_coin_amount,
            order.coin_coef,
            order.bonus_amount,
            order.final_coin_amount,
            order.route_information,
            order.assign_time,
            order.acquire_time,
            order.is_canceled
        ))
        conn.commit()


def update_order_acquire_time(order_id, acquire_time):
    with conn.cursor() as cursor:
        cursor.execute(f"""
            UPDATE orders
            SET acquire_time = '{acquire_time}'
            WHERE order_id = '{order_id}'
        """)
        conn.commit()


def get_order_from_db(order_id):
    with conn.cursor() as cursor:
        cursor.execute("""
        SELECT assign_order_id, order_id, executer_id, base_coin_amount, coin_coef, bonus_amount, final_coin_amount, route_information, assign_time, acquire_time, is_canceled
        FROM orders WHERE order_id = %s
        """, (order_id,))

        row = cursor.fetchone()
        if row:
            return AssignedOrder(
                assign_order_id=row[0],
                order_id=row[1],
                executer_id=row[2],
                base_coin_amount=row[3],
                coin_coef=row[4],
                bonus_amount=row[5],
                final_coin_amount=row[6],
                route_information=row[7],
                assign_time=row[8],
                acquire_time=row[9],
                is_canceled=row[10]
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


def cancel_order(order_id):
    with conn.cursor() as cursor:
        cursor.execute(f"""
            UPDATE orders
            SET is_canceled = True
            WHERE order_id = {order_id}
        """)
        conn.commit()


def close_db():
    conn.close()

from services.requests_handler import RequestHandler
from db import database as db
import logging
import json
import os

mock_host = os.getenv("MOCK_SERVER_HOST", "mock-server")
mock_port = os.getenv("MOCK_SERVER_PORT", "3629")
cancel_http = f'http://{mock_host}:{mock_port}/cancel-order'

logging.basicConfig(level=logging.DEBUG)

def outbox_fetch():
    canceled_orders = db.fetch_waiting()
    
    for order in canceled_orders:
        try:
            data = RequestHandler.fetch_data(cancel_http, params={'order_id': order[1]['order_id']})
            if data.get('status', 'error') == 'success':
                logging.debug(f"Order {order[1]['order_id']} has canceled!")
                db.success_on_cancel(order[0])
            else:
                db.error_on_cancel(order[0])
        except:
            db.error_on_cancel(order[0])



from services.requests_handler import RequestHandler
from services.cancelation import onCancel
from db import database as db
import logging
import json

logging.basicConfig(level=logging.INFO)

def outbox_fetch():
    while True:
        canceled_orders = db.fetch_waiting()
        logging.debug(f'{canceled_orders}')
        if not canceled_orders:
            break

        ids = [order[0] for order in canceled_orders]
        
        success = True
        for order in canceled_orders:
            try:
                payload = json.loads(order[1])
                onCancel(payload)
                
                logging.info(f"Order {payload['order_id']} has canceled!")
            except Exception as e:
                logging.warning(f"Error has occured: {e}")
                db.error_on_cancel()
                success = False
                break
        
        if success:
            db.success_on_cancel(ids)



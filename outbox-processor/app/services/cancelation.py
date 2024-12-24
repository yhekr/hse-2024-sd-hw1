from services.requests_handler import RequestHandler
import os 

mock_host = os.getenv("MOCK_SERVER_HOST", "mock-server")
mock_port = os.getenv("MOCK_SERVER_PORT", "3629")
cancel_http = f'http://{mock_host}:{mock_port}/cancel-order'

def onCancel(payload):
    RequestHandler.fetch_data(cancel_http, params={'order_id': payload['order_id']})
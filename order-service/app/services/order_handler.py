import uuid
from datetime import datetime
import grpc
from models.model import AssignedOrder
from db import database as db
from grpc_client.data_requests_pb2 import GetOrderInfoRequest
from grpc_client.data_requests_pb2_grpc import DataRequestsServiceStub

MAGIC_CONSTANT = 8 #можно вынести в конфиг наверное

db.init_db()

channel = grpc.insecure_channel("source_service:50051")
stub = DataRequestsServiceStub(channel)

def handle_assign_order_request(order_id: str, executer_id: str, locale: str):
    order_info = stub.GetOrderInfo(GetOrderInfoRequest(order_id=order_id, executer_id=executer_id))

    order_price = order_info.order_price
    executer_profile = order_info.executor_profile
    zone_display_name = order_info.zone_display_name

    order = AssignedOrder(
        assign_order_id=str(uuid.uuid4()),
        order_id=order_id,
        executer_id=executer_id,
        base_coin_amount=order_price.base_order_price,
        coin_coef=order_price.coin_coef,
        bonus_amount=order_price.coin_bonus_amount,
        final_coin_amount=order_price.final_order_price,
        route_information='',
        assign_time=datetime.now(),
        acquire_time=None,
        is_canceled=False
    )

    if executer_profile.rating >= MAGIC_CONSTANT:
        order.route_information = f'Order at zone "{zone_display_name}"'
    else:
        order.route_information = "Order at somewhere"

    print(f'>> New order handled! {order}')

    db.save_order_to_db(order)
    return order

def handle_acquire_order_request(executer_id: str):
    try:
        order_id = db.get_latest_order_id_for_executer(executer_id)
        if order_id:
            order_data = db.get_order_from_db(order_id)
            current_time = datetime.now()
            order_data.acquire_time = current_time
            db.update_order_acquire_time(order_data.order_id, current_time)
            print(f'>> Order acquired! Acquire time == {current_time - order_data.assign_time}')
            return order_data
        print()
        return None
    except KeyError:
        print(f'Order for executer ID "{executer_id}" not found!')
        return None

def handle_cancel_order_request(order_id: str):
    order_data = db.get_order_from_db(order_id)
    if order_data:
        db.cancel_order(order_id)
        print(f'>> Order was cancelled!')
        order_data.is_canceled = True
        return order_data
    else:
        print(f'Order ID "{order_id}" not found!')
        return None

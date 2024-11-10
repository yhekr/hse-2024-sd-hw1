import uuid
from datetime import datetime
import grpc
from models.model import AssignedOrder
from db import database as db
from grpc_client.data_requests_pb2 import OrderRequest, ZoneRequest, ExecuterRequest, TollRoadsRequest
from grpc_client.data_requests_pb2_grpc import DataRequestsServiceStub
from google.protobuf.empty_pb2 import Empty

MAGIC_CONSTANT = 8 #можно вынести в конфиг наверное

db.init_db()

channel = grpc.insecure_channel("source_service:50051")
stub = DataRequestsServiceStub(channel)

def handle_assign_order_request(order_id: str, executer_id: str, locale: str):
    # sequential gRPC requests but could be improved
    order_data = stub.GetOrderData(OrderRequest(order_id=order_id))
    zone_info = stub.GetZoneInfo(ZoneRequest(zone_id=order_data.zone_id))
    executer_profile = stub.GetExecuterProfile(ExecuterRequest(executer_id=executer_id))
    toll_roads = stub.GetTollRoads(TollRoadsRequest(zone_display_name=zone_info.display_name))
    print("Calling GetConfigs with request:", Empty())
    configs = stub.GetConfigs(Empty())

    actual_coin_coeff = zone_info.coin_coeff
    if configs.coin_coeff_settings:
        actual_coin_coeff = min(float(configs.coin_coeff_settings.get('maximum', '1')), actual_coin_coeff)
    final_coin_amount = order_data.base_coin_amount * actual_coin_coeff + toll_roads.bonus_amount

    order = AssignedOrder(
        str(uuid.uuid4()),
        order_id,
        executer_id,
        actual_coin_coeff,
        toll_roads.bonus_amount,
        final_coin_amount,
        '',
        datetime.now(),
        None
    )

    if executer_profile.rating >= MAGIC_CONSTANT:
        order.route_information = f'Order at zone "{zone_info.display_name}"'
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
            order_data.acquire_time = datetime.now()
            db.save_order_to_db(order_data)

            print(f'>> Order acquired! Acquire time == {order_data.acquire_time - order_data.assign_time}')
            return order_data
    except KeyError:
        print(f'Order for executer ID "{executer_id}" not found!')
        return None

def handle_cancel_order_request(order_id: str):
    order_data = db.get_order_from_db(order_id)
    if order_data:
        db.delete_order_from_db(order_id)
        print(f'>> Order was cancelled!')
        return order_data
    else:
        print(f'Order ID "{order_id}" not found!')
        return None

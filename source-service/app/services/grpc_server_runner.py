import grpc
from concurrent import futures
import time
from grpc_server import data_requests_pb2_grpc
from grpc_server.data_requests_pb2 import GetOrderInfoResponse, OrderPrice, ExecuterProfile
from services import data_requests


class DataRequestsService(data_requests_pb2_grpc.DataRequestsServiceServicer):
    """Implementation of the gRPC methods defined in data_requests.proto."""

    def GetOrderInfo(self, request, context):
        order_data = data_requests.get_order_data(request.order_id)

        zone_info = data_requests.get_zone_info(order_data.zone_id)

        toll_roads = data_requests.get_toll_roads(zone_info.display_name)

        executer_profile = data_requests.get_executer_profile(request.executer_id)

        configs = data_requests.get_configs()

        actual_coin_coeff = zone_info.coin_coeff
        if configs.coin_coeff_settings:
            actual_coin_coeff = min(float(configs.coin_coeff_settings.get('maximum', '1')), actual_coin_coeff)
        final_order_price = order_data.base_coin_amount * actual_coin_coeff + toll_roads.bonus_amount

        return GetOrderInfoResponse(
            order_price=OrderPrice(
                base_order_price=order_data.base_coin_amount,
                coin_coef=zone_info.coin_coeff,
                coin_bonus_amount=toll_roads.bonus_amount,
                final_order_price=final_order_price
            ),
            zone_display_name=zone_info.display_name,
            executor_profile=ExecuterProfile(
                id=executer_profile.id,
                tags=executer_profile.tags,
                rating=executer_profile.rating
            )
        )


def serve():
    # Set up the gRPC server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    data_requests_pb2_grpc.add_DataRequestsServiceServicer_to_server(DataRequestsService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC server is running on port 50051.")

    try:
        while True:
            time.sleep(86400)  # Keep the server running for a day
    except KeyboardInterrupt:
        print("Shutting down gRPC server.")
        server.stop(0)


if __name__ == "__main__":
    serve()

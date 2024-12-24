import grpc
from concurrent import futures
import time
from grpc_server import data_requests_pb2_grpc
from grpc_server.data_requests_pb2 import GetOrderInfoResponse, OrderPrice, ExecuterProfile
from services import data_requests
from models.model import Info 
from services.order_info import get_order_info


class DataRequestsService(data_requests_pb2_grpc.DataRequestsServiceServicer):
    """Implementation of the gRPC methods defined in data_requests.proto."""

    def GetOrderInfo(self, request, context):
        info = get_order_info(request)

        actual_coin_coeff = info.zone_data.coin_coeff
        if info.config_map.coin_coeff_settings:
            actual_coin_coeff = min(float(info.config_map.coin_coeff_settings.get('maximum', '1')), actual_coin_coeff)
        final_order_price = info.order_data.base_coin_amount * actual_coin_coeff + info.toll_roads_data.bonus_amount

        return GetOrderInfoResponse(
            order_price=OrderPrice(
                base_order_price=info.order_data.base_coin_amount,
                coin_coef=info.zone_data.coin_coeff,
                coin_bonus_amount=info.toll_roads_data.bonus_amount,
                final_order_price=final_order_price
            ),
            zone_display_name=info.zone_data.display_name,
            executor_profile=ExecuterProfile(
                id=info.executer_profile.id,
                tags=info.executer_profile.tags,
                rating=info.executer_profile.rating
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

import grpc
from concurrent import futures
import time
from grpc_server import data_requests_pb2_grpc, data_requests_pb2
from services import data_requests


class DataRequestsService(data_requests_pb2_grpc.DataRequestsServiceServicer):
    """Implementation of the gRPC methods defined in data_requests.proto."""

    def GetOrderData(self, request, context):
        # Retrieve order data based on order_id from the request
        order_data = data_requests.get_order_data(request.order_id)
        return data_requests_pb2.OrderData(
            id=order_data.id,
            user_id=order_data.user_id,
            zone_id=order_data.zone_id,
            base_coin_amount=order_data.base_coin_amount
        )

    def GetZoneInfo(self, request, context):
        # Retrieve zone information based on zone_id from the request
        zone_info = data_requests.get_zone_info(request.zone_id)
        return data_requests_pb2.ZoneData(
            id=zone_info.id,
            coin_coeff=zone_info.coin_coeff,
            display_name=zone_info.display_name
        )

    def GetExecuterProfile(self, request, context):
        # Retrieve executer profile based on executer_id from the request
        executer_profile = data_requests.get_executer_profile(request.executer_id)
        return data_requests_pb2.ExecuterProfile(
            id=executer_profile.id,
            tags=executer_profile.tags,
            rating=executer_profile.rating
        )

    def GetConfigs(self, request, context):
        # Retrieve configuration settings
        configs = data_requests.get_configs()
        return data_requests_pb2.ConfigData(
            coin_coeff_settings=configs.coin_coeff_settings
        )

    def GetTollRoads(self, request, context):
        # Retrieve toll roads data based on zone_display_name from the request
        toll_roads = data_requests.get_toll_roads(request.zone_display_name)
        return data_requests_pb2.TollRoadsData(
            bonus_amount=toll_roads.bonus_amount
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

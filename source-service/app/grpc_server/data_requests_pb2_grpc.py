# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import data_requests_pb2 as data__requests__pb2


class DataRequestsServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetOrderData = channel.unary_unary(
                '/datarequests.DataRequestsService/GetOrderData',
                request_serializer=data__requests__pb2.OrderRequest.SerializeToString,
                response_deserializer=data__requests__pb2.OrderData.FromString,
                )
        self.GetZoneInfo = channel.unary_unary(
                '/datarequests.DataRequestsService/GetZoneInfo',
                request_serializer=data__requests__pb2.ZoneRequest.SerializeToString,
                response_deserializer=data__requests__pb2.ZoneData.FromString,
                )
        self.GetExecuterProfile = channel.unary_unary(
                '/datarequests.DataRequestsService/GetExecuterProfile',
                request_serializer=data__requests__pb2.ExecuterRequest.SerializeToString,
                response_deserializer=data__requests__pb2.ExecuterProfile.FromString,
                )
        self.GetConfigs = channel.unary_unary(
                '/datarequests.DataRequestsService/GetConfigs',
                request_serializer=data__requests__pb2.Empty.SerializeToString,
                response_deserializer=data__requests__pb2.ConfigData.FromString,
                )
        self.GetTollRoads = channel.unary_unary(
                '/datarequests.DataRequestsService/GetTollRoads',
                request_serializer=data__requests__pb2.TollRoadsRequest.SerializeToString,
                response_deserializer=data__requests__pb2.TollRoadsData.FromString,
                )


class DataRequestsServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetOrderData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetZoneInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetExecuterProfile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetConfigs(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTollRoads(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DataRequestsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetOrderData': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOrderData,
                    request_deserializer=data__requests__pb2.OrderRequest.FromString,
                    response_serializer=data__requests__pb2.OrderData.SerializeToString,
            ),
            'GetZoneInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetZoneInfo,
                    request_deserializer=data__requests__pb2.ZoneRequest.FromString,
                    response_serializer=data__requests__pb2.ZoneData.SerializeToString,
            ),
            'GetExecuterProfile': grpc.unary_unary_rpc_method_handler(
                    servicer.GetExecuterProfile,
                    request_deserializer=data__requests__pb2.ExecuterRequest.FromString,
                    response_serializer=data__requests__pb2.ExecuterProfile.SerializeToString,
            ),
            'GetConfigs': grpc.unary_unary_rpc_method_handler(
                    servicer.GetConfigs,
                    request_deserializer=data__requests__pb2.Empty.FromString,
                    response_serializer=data__requests__pb2.ConfigData.SerializeToString,
            ),
            'GetTollRoads': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTollRoads,
                    request_deserializer=data__requests__pb2.TollRoadsRequest.FromString,
                    response_serializer=data__requests__pb2.TollRoadsData.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'datarequests.DataRequestsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DataRequestsService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetOrderData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/datarequests.DataRequestsService/GetOrderData',
            data__requests__pb2.OrderRequest.SerializeToString,
            data__requests__pb2.OrderData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetZoneInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/datarequests.DataRequestsService/GetZoneInfo',
            data__requests__pb2.ZoneRequest.SerializeToString,
            data__requests__pb2.ZoneData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetExecuterProfile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/datarequests.DataRequestsService/GetExecuterProfile',
            data__requests__pb2.ExecuterRequest.SerializeToString,
            data__requests__pb2.ExecuterProfile.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetConfigs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/datarequests.DataRequestsService/GetConfigs',
            data__requests__pb2.Empty.SerializeToString,
            data__requests__pb2.ConfigData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTollRoads(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/datarequests.DataRequestsService/GetTollRoads',
            data__requests__pb2.TollRoadsRequest.SerializeToString,
            data__requests__pb2.TollRoadsData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
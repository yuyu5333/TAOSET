# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from ar_dist.proto import ar_pb2 as ar__pb2
from ar_dist.proto import common_pb2 as common__pb2


class RingAllReduceServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.VariableWeightsInit = channel.unary_unary(
                '/RingAllReduceService/VariableWeightsInit',
                request_serializer=common__pb2.ResDictionary.SerializeToString,
                response_deserializer=common__pb2.ResDictionary.FromString,
                )
        self.Recieve = channel.unary_unary(
                '/RingAllReduceService/Recieve',
                request_serializer=ar__pb2.RingAllReduceReq.SerializeToString,
                response_deserializer=ar__pb2.RingAllReduceResp.FromString,
                )


class RingAllReduceServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def VariableWeightsInit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Recieve(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RingAllReduceServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'VariableWeightsInit': grpc.unary_unary_rpc_method_handler(
                    servicer.VariableWeightsInit,
                    request_deserializer=common__pb2.ResDictionary.FromString,
                    response_serializer=common__pb2.ResDictionary.SerializeToString,
            ),
            'Recieve': grpc.unary_unary_rpc_method_handler(
                    servicer.Recieve,
                    request_deserializer=ar__pb2.RingAllReduceReq.FromString,
                    response_serializer=ar__pb2.RingAllReduceResp.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'RingAllReduceService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RingAllReduceService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def VariableWeightsInit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/RingAllReduceService/VariableWeightsInit',
            common__pb2.ResDictionary.SerializeToString,
            common__pb2.ResDictionary.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Recieve(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/RingAllReduceService/Recieve',
            ar__pb2.RingAllReduceReq.SerializeToString,
            ar__pb2.RingAllReduceResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
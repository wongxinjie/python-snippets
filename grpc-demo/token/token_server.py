import time
import hashlib
import logging
from concurrent import futures
from functools import wraps

import grpc

import key_pb2
import key_pb2_grpc

_SLEEP = 60 * 60 * 24

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s# %(message)s",
    datefmt="%Y/%m/%d-%H:%M:%S"
)


def trace(func):
    @wraps(func)
    def wrapper(self, request, context):
        start = time.time()
        method_name = func.__name__
        logging.info("%s request: %s", method_name, str(request))
        result = func(self, request, context)
        print(time.time() - start)
        interval = (time.time() - start) * 1000
        logging.info("%s response:  %.2f ms" % (method_name, interval))
        return result

    return wrapper


class TokenServer(key_pb2_grpc.TokenServicer):

    @trace
    def generate(self, request, context):
        key = request.key
        logging.info("GET key => %s", key)
        token = hashlib.md5(key.encode('utf-8')).hexdigest()
        logging.info("Return token => %s", token)
        return key_pb2.TokenResponse(token=token)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    key_pb2_grpc.add_TokenServicer_to_server(TokenServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()

    try:
        while True:
            time.sleep(_SLEEP)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    serve()

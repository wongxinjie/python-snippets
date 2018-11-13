import time
import grpc

import key_pb2
import key_pb2_grpc


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = key_pb2_grpc.TokenStub(channel)
    response = stub.generate(key_pb2.TokenRequest(key='密钥'))
    print('Token => ', response.token)


if __name__ == "__main__":
    start = time.time()
    run()
    print((time.time() - start) * 1000, 'ms')

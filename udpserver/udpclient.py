import uuid
import time
import asyncio
import socket
import concurrent.futures


class EchoClientProtocol:

    def __init__(self, message, loop):
        self.message = message
        self.loop = loop
        self.transport = None

    def connection_made(self, transport):
        self.transport = transport
        print('Send => ', self.message)
        self.transport.sendto(self.message.encode())

    def datagram_received(self, data, addr):
        print("Received => ", data.decode())
        print("Close the socket")
        self.transport.close()

    def error_received(self, exc):
        print("Wrror received: ", exc)

    def connection_lost(self, exc):
        print("Socket closed")
        loop = asyncio.get_event_loop()
        loop.stop()


def main():
    loop = asyncio.get_event_loop()
    message = '{}:Python'.format(str(uuid.uuid4()))
    connect = loop.create_datagram_endpoint(
        lambda: EchoClientProtocol(message, loop),
        remote_addr=('127.0.0.1', 9000)
    )
    transport, protocol = loop.run_until_complete(connect)
    loop.run_forever()
    transport.close()
    loop.close()


def client(name):
    server_address = ('localhost', 9000)
    message = '{}:{}'.format(str(uuid.uuid4()), name)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.sendto(message.encode('utf-8'), server_address)
        sock.settimeout(1)
        data, server = sock.recvfrom(4096)
        print('server => ', server, type(server))
        print('client => %s, data => %s' % (name, data.decode("utf-8")))
    except Exception as err:
        print(err)
    finally:
        sock.close()


def concurrent_visit(count=100):
    start = time.time()
    args = ['User-{}'.format(n) for n in range(count)]
    with concurrent.futures.ThreadPoolExecutor(max_workers=count) as excutor:
        excutor.map(client, args)
    print('Take => %.8fs' % (time.time() - start))

if __name__ == "__main__":
    concurrent_visit()

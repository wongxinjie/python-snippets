import time
import hashlib
import asyncio
import socket
import socketserver

import curio
from tornado.ioloop import IOLoop
from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
from curio import socket as curio_socket

from udp import BaseUDPServer


def salt(text):
    if not isinstance(text, bytes):
        text = str(text).encode('utf-8')

    md5 = hashlib.md5()
    md5.update(text)
    token = md5.hexdigest().upper()
    return token


def process(data, addr):
    message = data.decode()
    request_id, message = message.split(':')
    print('From: %s, RequestID: %s, Message: %s' % (
        '{}:{}'.format(*addr), request_id, message
    ))
    token = salt(message)
    message = 'Token:{}'.format(token)
    print('%s => %r' % (message, addr))
    return message.encode('utf-8')


class EchoServerProtocol(asyncio.DatagramProtocol):

    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, addr):
        start = time.time()
        message = process(data, addr)
        self.transport.sendto(message, addr)
        print('asyncio take => ',  time.time() - start)

    def connection_lost(self, exc):
        print('Connection lost', exc)


def asyncio_upd_server():
    host, port = '127.0.0.1', 9000
    print('Run UDP server on {}:{}'.format(host, port))
    loop = asyncio.get_event_loop()
    listen = loop.create_datagram_endpoint(
        EchoServerProtocol,
        local_addr=(host, port)
    )
    transport, protocol = loop.run_until_complete(listen)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    transport.close()
    loop.close()


def socket_udp_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 9000)
    print('Run UDP server on {}:{}'.format(*server_address))
    sock.bind(server_address)

    while True:
        start = time.time()
        data, address = sock.recvfrom(4096)
        message = process(data, address)
        sock.sendto(message, address)
        print('socket take => ',  time.time() - start)


class UDPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        start = time.time()
        data = self.request[0].strip()
        sock = self.request[1]
        message = process(data, self.client_address)
        sock.sendto(message, self.client_address)
        print('socketserver take => ',  time.time() - start)


def socketserver_udp_server():
    server_address = ('localhost', 9000)
    print('Run UDP server on {}:{}'.format(*server_address))
    server = socketserver.UDPServer(server_address, UDPHandler)
    server.serve_forever()


class UDPServer(BaseUDPServer):
    def on_recive(self, data, address):
        message = process(data, address)
        print(message)


def weak_tornado_udp_server():
    host, port = '127.0.0.1', 9000
    print('Run UDP server on {}:{}'.format(host, port))
    server = UDPServer()
    server.bind(9000)
    server.start()
    IOLoop.instance().start()


class TwistedUDPServer(DatagramProtocol):

    def datagramReceived(self, data, addr):
        message = process(data, addr)
        self.transport.write(message, addr)


def twisted_udp_server():
    host, port = '127.0.0.1', 9000
    print('Run UDP server on {}:{}'.format(host, port))
    reactor.listenUDP(9000, TwistedUDPServer())
    reactor.run()


async def _curio_udp_server():
    host, port = '127.0.0.1', 9000
    print('Run UDP server on {}:{}'.format(host, port))
    sock = curio_socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, port))

    while True:
        data, addr = await sock.recvfrom(4096)
        message = process(data, addr)
        await sock.sendto(message, addr)


def curio_udp_server():
    curio.run(_curio_udp_server)


if __name__ == "__main__":
    asyncio_upd_server()
    # socket_udp_server()
    # socketserver_udp_server()
    # weak_tornado_udp_server()
    # twisted_udp_server()
    # curio_udp_server()

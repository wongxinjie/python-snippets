import time
import socket


def socket_udp_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('0.0.0.0', 1812)
    print('Run UDP server on {}:{}'.format(*server_address))
    sock.bind(server_address)

    while True:
        start = time.time()
        data, address = sock.recvfrom(4096)
        print(data)
        print(address)
        # message = process(data, address)
        message = b'OK'
        sock.sendto(message, address)
        print('socket take => ',  time.time() - start)


if __name__ == "__main__":
    socket_udp_server()

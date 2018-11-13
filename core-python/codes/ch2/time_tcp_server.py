import socket
from time import ctime

import utils


HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(ADDR)
sock.listen(5)

while True:
    print("waiting for connection...")
    client_sock, addr = sock.accept()
    print("connection from: ", addr)

    while True:
        data = client_sock.recv(BUFSIZE)
        if not data:
            break
        msg = '[%s] %s' % (ctime(), utils.ensure_unicode(data))
        print('Received: ', msg)
        client_sock.send(utils.ensure_bytes(msg))
    client_sock.close()
sock.close()

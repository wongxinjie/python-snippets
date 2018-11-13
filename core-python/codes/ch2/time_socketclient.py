import socket

import utils

HOST = 'localhost'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)


msgs = ['SYN=1, ACK=1\r\n', 'ACK=1\r\n', '\r\n']
for msg in msgs:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(ADDR)
    sock.send(utils.ensure_bytes(msg))
    data = sock.recv(BUFSIZE)
    print(utils.ensure_unicode(data))

sock.close()

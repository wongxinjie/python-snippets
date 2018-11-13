import socket

import utils

HOST = 'localhost'
service = 'daytime'

port = socket.getservbyname(service)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect((HOST, port))
sock.send(utils.ensure_bytes(service))
data = sock.recvfrom(1024)
print(utils.ensure_unicode(data))
sock.close()

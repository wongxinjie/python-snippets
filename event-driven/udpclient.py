import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(b'', ('localhost', 14000))
print(s.recvfrom(128))

s.sendto(b'Hello', ('localhost', 15000))
print(s.recvfrom(128))

import socket
import sys

host, port = "localhost", 9000
data = " ".join(sys.argv[1:])


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(bytes(data+"\n", "utf-8"), (host, port))
received = str(sock.recv(2048), "utf-8")

print("Sent => ", data)
print("Received => ", received)

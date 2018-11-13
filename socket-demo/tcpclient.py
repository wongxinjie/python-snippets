import socket
import sys

host, port = "localhost", 9000
data = " ".join(sys.argv[1:])


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((host, port))
    sock.sendall(bytes(data+"\n", "utf-8"))
    received = str(sock.recv(2048), "utf-8")

print("Sent => ", data)
print("Received => ", received)

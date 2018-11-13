import socket
import time

from eventloop import Event, event_loop


class UDPServer(Event):

    def __init__(self, address):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(address)

    def fileno(self):
        return self.sock.fileno()

    def receive_ready(self):
        return True


class UDPTimeServer(UDPServer):

    def handle_receive(self):
        msg, addr = self.sock.recvfrom(1)
        self.sock.sendto(time.ctime().encode('ascii'), addr)


class UDPEchoServer(UDPServer):

    def handle_receive(self):
        msg, addr = self.sock.recvfrom(8192)
        self.sock.sendto(msg, addr)


if __name__ == "__main__":
    handlers = [UDPTimeServer(('', 14000)), UDPEchoServer(('', 15000))]
    event_loop(handlers)

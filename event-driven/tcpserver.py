import socket

from eventloop import Event, event_loop


class TCPServer(Event):

    def __init__(self, address, client_handler, handler_list):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(address)
        self.sock.listen(1)
        self.client_handler = client_handler
        self.handler_list = handler_list

    def fileno(self):
        return self.sock.fileno()

    def receive_ready(self):
        return True

    def handle_receive(self):
        client, addr = self.sock.accept()
        self.handler_list.append(self.client_handler(client, self.handler_list))


class TCPClient(Event):
    def __init__(self, sock, handler_list):
        self.sock = sock
        self.handler_list = handler_list
        self.outgoing = bytearray()

    def fileno(self):
        return self.sock.fileno()

    def close(self):
        self.sock.close()
        self.handler_list.remove(self)

    def send_ready(self):
        return True if self.outgoing else False

    def handle_send(self):
        nsent = self.sock.send(self.outgoing)
        self.outgoing = self.outgoing[nsent:]


class TCPEchoClient(TCPClient):

    def receive_ready(self):
        return True

    def handle_receive(self):
        data = self.sock.recv(8192)
        print(data)
        if not data.strip():
            self.close()
        else:
            self.outgoing.extend(data.upper())


if __name__ == "__main__":
    handlers = []
    handlers.append(TCPServer(('', 16000), TCPEchoClient, handlers))
    event_loop(handlers)

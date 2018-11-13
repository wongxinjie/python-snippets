import socketserver


class SimpleTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        self.data = self.request.recv(2048).strip()
        print("{} wrote: ".format(self.client_address[0]))
        print(self.data)
        self.request.sendall(self.data.upper())


def serve():
    host, port = 'localhost', 9000
    print('Run TCPServer in {}:{}'.format(host, port))
    server = socketserver.TCPServer((host, port), SimpleTCPHandler)
    server.serve_forever()


if __name__ == "__main__":
    serve()

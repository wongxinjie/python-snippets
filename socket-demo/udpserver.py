import socketserver


class SimpleUDPServer(socketserver.BaseRequestHandler):

    def handle(self):
        print('request => ', self.request)
        data = self.request[0].strip()
        socket = self.request[1]
        print('client_address =>', self.client_address)
        print("{} wrote: ".format(self.client_address[0]))
        print('data => ', data)
        socket.sendto(data.upper(), self.client_address)


def serve():
    host, port = "localhost", 9000
    print("Run UDPServer on {}:{}".format(host, port))
    server = socketserver.UDPServer((host, port), SimpleUDPServer)
    server.serve_forever()


if __name__ == "__main__":
    serve()

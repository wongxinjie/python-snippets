import select
import socket
import signal

BUFSIZE = 2048


class ChatServer:

    def __init__(self, port=5000, backlog=128):
        self.clients = 0
        self.client_map = {}
        self.outputs = []

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind(('', port))
        print('listening to port' % port)
        self.server.listen(backlog)
        signal.signal(signal.SIGINT, self.sighandler)

    def sighandler(self, signum, frame):
        print("shutting down server...")
        for s in self.outputs:
            s.close()
        self.server.close()

    def get_name(self, sock):
        info = self.client_map[sock]
        host, name = info[0][0], info[1]
        return '@'.join((name, host))

    def serve(self):
        inputs = [self.server]
        outputs = []
        running = 1

        while running:
            try:
                readables, writables, errors = select.select(
                    inputs, self.outputs, [])
            except socket.error as err:
                print(err)
                break

            for s in readables:
                if s == self.server:
                    client, address = self.server.accept()
                    print('chatserver: got connection %d from %s' % (client.fileno(), address))

from socketserver import TCPServer
from socketserver import StreamRequestHandler
from time import ctime

import utils

HOST = ''
PORT = 21567
ADDR = (HOST, PORT)


class TimeRequestHandler(StreamRequestHandler):

    def handle(self):
        print("...connection from: ", self.client_address)
        msg = '[%s] %s' % (ctime(), utils.ensure_unicode(self.rfile.readline()).strip())
        print(msg)
        self.wfile.write(utils.ensure_bytes(msg))


tcp_server = TCPServer(ADDR, TimeRequestHandler)
try:
    tcp_server.serve_forever()
except KeyboardInterrupt as err:
    tcp_server.shutdown()

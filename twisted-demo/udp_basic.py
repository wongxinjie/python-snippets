from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


class Echo(DatagramProtocol):

    def datagramReceived(self, data, addr):
        print("received: %r from %s" % (data, addr))
        self.transport.write(data, addr)


if __name__ == "__main__":
    print('run UDP server on => ', 9000)
    reactor.listenUDP(9000, Echo())
    reactor.run()

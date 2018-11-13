from twisted.internet import reactor, protocol


class EchoClient(protocol.Protocol):

    def connectionMade(self):
        self.transport.write('Hello, World!'.encode('utf-8'))

    def dataReceived(self, data):
        print('Server said: ', data)
        self.transport.loseConnection()


class EchoFactory(protocol.ClientFactory):

    def buildProtocol(self, addr):
        return EchoClient()

    def clientConnectionFailed(self, connector, reason):
        print("Connection failed")
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print("Connection lost.")
        reactor.stop()


if __name__ == "__main__":
    print('Run')
    reactor.connectTCP("localhost", 8000, EchoFactory())
    reactor.run()

from twisted.internet import reactor
from chatserver import ChatFactory

reactor.listenTCP(8000, ChatFactory())
reactor.run()


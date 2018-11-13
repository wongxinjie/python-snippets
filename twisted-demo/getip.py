from twisted.internet import reactor


def gotIP(ip):
    print("IP of 'localhot' is ", ip)
    reactor.stop()


reactor.resolve('localhost').addCallback(gotIP)
reactor.run()

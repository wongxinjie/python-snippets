from twisted.application.service import IServiceMaker
from twisted.application import internet
from twisted.plugin import IPlugin
from twisted.python import usage
from zope.interface import implements

from nonblocking import pageFactory


class Options(usage.Options):
    optParammeters = [['port', 'p', 8000, 'The port number to listen on.']]


class PageServiceMarker(object):
    implements(IServiceMaker, IPlugin)
    tapname = "page"
    description = "A non-blocking echo server"
    options = Options

    def makeService(self, options):
        return internet.TCPServer(int(options['port']), pageFactory)


serviceMaker = PageServiceMarker()

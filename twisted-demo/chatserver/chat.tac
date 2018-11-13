from twisted.application import internet, service
from chatserver import ChatFactory


application = service.Application("chatserver")
chatService = internet.TCPServer(8000, ChatFactory())
chatService.setServiceParent(application)

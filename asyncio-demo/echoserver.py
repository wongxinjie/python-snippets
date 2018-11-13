import asyncio
import time


class EchoProtocol(asyncio.Protocol):

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        print('received => ', data)
        # asyncio.sleep(20)
        time.sleep(30)
        self.transport.write(data)

    def connection_lost(self, exc):
        print('connection lost')


loop = asyncio.get_event_loop()
server = loop.run_until_complete(
    loop.create_server(EchoProtocol, 'localhost', 9000))
loop.run_until_complete(server.wait_closed())

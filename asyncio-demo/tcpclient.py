import asyncio


class EchoClientProtocol(asyncio.Protocol):

    def __init__(self, message, loop):
        self.message = message
        self.loop = loop

    def connection_made(self, transport):
        transport.write(self.message.encode())
        print('Data sent: {!r}'.format(self.message))

    def data_received(self, data):
        print('Data received: {!r}'.format(data.decode()))

    def connection_lost(self, exc):
        print('The server close connection')
        print('Stop the event loop')
        self.loop.stop()


async def tcp_echo_client(messge, loop):
    reader, writer = await asyncio.open_connection("127.0.0.1", 9000, loop=loop)

    print("Send: %r" % messge)
    writer.write(messge.encode())

    data = await reader.read(128)
    print("Received: %r" % data.decode())

    print("Close socket")
    writer.close()

loop = asyncio.get_event_loop()
message = 'Python vs Go'
# coro = loop.create_connection(
#     lambda: EchoClientProtocol(message, loop), '127.0.0.1', 9000
# )
# loop.run_until_complete(coro)
loop.run_until_complete(tcp_echo_client(message, loop))
loop.close()

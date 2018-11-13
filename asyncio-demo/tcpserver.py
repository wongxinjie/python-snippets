import asyncio


class EchoServerProtocol(asyncio.Protocol):

    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = transport

    def data_received(self, data):
        message = data.decode('utf-8')
        print('Data received: {!r}'.format(message))

        print('Send : {!r}'.format(message))
        self.transport.write(data)

        print('Close the client socket')
        self.transport.close()


async def handle_socket(reader, writer):
    data = await reader.read(128)
    message = data.decode()
    address = writer.get_extra_info("peername")
    print("Received %r from %r" % (message, address))

    print("Send: %r" % message)
    writer.write(data)
    await writer.drain()
    print("Close the client socket.")
    writer.close()


loop = asyncio.get_event_loop()
# coro = loop.create_server(EchoServerProtocol, '127.0.0.1', 9000)
coro = asyncio.start_server(handle_socket, "127.0.0.1", 9000, loop=loop)
server = loop.run_until_complete(coro)

print('Server on {}'.format(server.sockets[0].getsockname()))

try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

server.close()
loop.run_until_complete(server.wait_closed())
loop.close()

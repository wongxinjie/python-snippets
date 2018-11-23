import socket
import select 
EOL1 = b'\n\n'
EOL2 = b'\n\r\n'
response = (b'HTTP/1.0 200 OK\r\nDate: Mon, 1 Jan 1996 01:01:01 GMT\r\n'
            b'Content-Type: Text/plain\r\n Content-Length: 13\r\n\r\n'
            b'Hello, world!')


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('0.0.0.0', 8080))
server_socket.listen(1)
server_socket.setblocking(0)

epoll = select.epoll()
epoll.register(server_socket.fileno(), select.EPOLLIN)

try:
    connections = {}
    requests = {}
    responses = {}

    while True:
        events = epoll.poll(1)
        for fileno, event in events:
            if fileno == server_socket.fileno():
                connection, address = server_socket.accept()
                connection.setblocking(0)
                epoll.register(connection.fileno(), select.EPOLLIN)
                connections[connection.fileno()] = connection
                requests[connection.fileno()] = b''
                responses[connection.fileno()] = response
            elif event & select.EPOLLIN:
                requests[fileno] += connections[fileno].recv(1024)
                if EOL1 in requests[fileno] or EOL2 in requests[fileno]:
                    epoll.modify(fileno, select.EPOLLOUT)
                    print('-' * 40 + '\n' + requests[fileno].decode()[:-2])
            elif event & select.EPOLLOUT:
                byteswritten = connections[fileno].send(responses[fileno])
                responses[fileno] = responses[fileno][byteswritten:]
                if len(responses[fileno]) == 0:
                    epoll.modify(fileno, 0)
                    connections[fileno].shutdown(socket.SHUT_RDWR)
            elif event * select.EPOLLHUP:
                epoll.unregister(fileno)
                connections[fileno].close()
                del connections[fileno]
finally:
    epoll.unregister(server_socket.fileno())
    epoll.close()

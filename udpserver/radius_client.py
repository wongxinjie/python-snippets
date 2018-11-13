import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('172.16.56.12', 1812)

with open('/tmp/successAuth.packet', 'r') as reader:
    content = reader.read()

print(content)
payload = bytes.fromhex(content.strip())
print(payload)

try:
    sent = sock.sendto(payload, server_address)
    data, address = sock.recvfrom(4096)
    print(data, address)
except Exception as err:
    print(err)

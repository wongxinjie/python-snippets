# import struct
# ip = '127.56.8.14'
# _FMT = ">B4sB"
# data = struct.pack(_FMT, 12, ip.encode('utf-8'), 7)
# print(data)
# print(struct.unpack(_FMT, data))

mac = "FF:FF:FF:FF:FF"


def c(mac):
    macs = mac.split(':')
    return ''.join([chr(int(rv, base=16)) for rv in macs])


def r(macbytes):
    macs = []
    for c in macbytes:
        rv = hex(ord(c))[2:].upper()
        macs.append(rv)

    return ':'.join(macs)

data = c(mac)
print('R => ', r(data))

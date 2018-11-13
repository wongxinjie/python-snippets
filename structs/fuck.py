import struct


class Header():
    '''
        ver     : portal protocol version 0x01 | 0x02
        type    : 0x01 ~ 0x0a
        auth    : Chap 0x00 | Pap 0x01
        rsv     : reserve byte always 0x00
        serial  : serial number
        req     : req id
        ip      : user ip (wlan user's ip)
        port    : haven't used, always 0
        err     : error code
        num     : attribute number
    '''
    _FMT = '>BBBBHH4sHBB'

    def __init__(self, ver, type, auth, rsv, serial, req, ip, port, err, num):
        self.ver = ver
        self.type = type
        self.auth = auth
        self.rsv = rsv
        self.serial = serial
        self.req = req
        self.ip = ip
        self.port = port
        self.err = err
        self.num = num
        # self.auth = b'0'*16

    def pack(self):
        '''
            return binary data in big-endian[>]
        '''
        return struct.pack(self._FMT,
                           self.ver, self.type, self.auth, self.rsv,
                           self.serial, self.req, self.ip, self.port,
                           self.err, self.num)

    @classmethod
    def unpack(cls, data):
        '''
            check & parse data, return new instance
        '''
        if len(data) < 16:
            raise ValueError('Read Data length abnormal')
        return cls(*struct.unpack(cls._FMT, data[:16]))

header = Header(0x01, 0x01, 0x00, 0x00, 123, 0, "127.0.0.1", 0, 0x00, 0x00)
data = header.pack()
print(data)

h = Header.unpack(data)
print(h.ip)

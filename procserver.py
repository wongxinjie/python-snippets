from multiprocessing.managers import BaseManager

host = '0.0.0.0'
port = 19030
authkey = 'key'


share_list = []


class RemoteManager(BaseManager):
    pass

RemoteManager.register('get_list', callable=lambda: share_list)
mgr = RemoteManager(address=(host, port), authkey=authkey)
server = mgr.get_server()
server.serve_forever()

import threading
from multiprocessing.managers import BaseManager


host = '192.168.1.221'
port = 9030
authkey = b'key'


class RemoteManager(BaseManager):
    pass

RemoteManager.register('get_list')
mgr = RemoteManager(address=(host, port), authkey=authkey)


def func(n):
    print('thread-%s' % n)
    mgr.connect()
    l = mgr.get_list()
    l.append(n)
    print(mgr.get_list())


def main():

    threads = [threading.Thread(target=func, args=(n, ))
               for n in range(10)]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


main()

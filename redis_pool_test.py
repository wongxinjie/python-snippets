import time
import threading

import redis

REDIS_CONNECTION_POOL = redis.ConnectionPool(host='localhost',
                                             port=6379)
rdb = redis.StrictRedis()
key = 'test:block:timeout'


def block_operation(timeout):
    start = time.time()
    # rdb = redis.StrictRedis(connection_pool=REDIS_CONNECTION_POOL)
    rdb.blpop(key, timeout=timeout)
    print('timeout=%s, cost=%s' % (timeout, time.time() - start))
    print(rdb.get(key))
    rdb.set(key, timeout)


def main():
    timeouts = [4, 8, 10, 12]
    threads = [threading.Thread(target=block_operation, args=(timeout, ))
               for timeout in timeouts]

    start = time.time()
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("@@MAIN cost=%s" % (time.time() - start))


main()

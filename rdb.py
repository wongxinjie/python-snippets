# coding: utf-8
import os
import time
import math
import uuid
import json
from multiprocessing import Pool

import redis

rdb = redis.Redis()
key = 'test:concurrent:key'


def acquire_lock(conn, lockname, acquire_timeout=10, lock_timeout=10):
    identifier = str(uuid.uuid4())
    lock_timeout = int(math.ceil(lock_timeout))

    end = time.time() + acquire_timeout
    while time.time() < end:
        if conn.setnx(lockname, identifier):
            conn.expire(lockname, lock_timeout)
            return identifier
        elif not conn.ttl(lockname):
            conn.expire(lockname, lock_timeout)
    return ''


def release_lock(conn, lockname, identifier):
    pipe = conn.pipeline()

    while True:
        try:
            pipe.watch(lockname)
            print(type(pipe.get(lockname)), type(identifier))
            if pipe.get(lockname).decode() == identifier:
                pipe.multi()
                pipe.delete(lockname)
                pipe.execute()
                return True
            pipe.unwatch()
            break
        except redis.exceptions.WatchError as err:
            pass
    return False


def change():
    lockname = 'lock:{}'.format(key)

    while True:
        lock = acquire_lock(rdb, lockname)
        if lock:
            break

    with rdb.pipeline() as pipe:
        try:
            pipe.watch(key)
            rv = pipe.get(key)
            if not rv:
                rv = {'count': 0}
            else:
                rv = json.loads(rv.decode())

            rv['count'] += 1
            pipe.set(key, json.dumps(rv))
            pipe.execute()
            pipe.unwatch()
        except redis.exceptions.WatchError as err:
            pass
        finally:
            release_lock(rdb, lockname, lock)


if __name__ == "__main__":
    print("Processing...")
    rdb.delete(key)

    p = Pool()
    for n in range(5):
        p.apply_async(change, args=())

    p.close()
    p.join()

    rv = rdb.get(key)
    print(rv.decode())

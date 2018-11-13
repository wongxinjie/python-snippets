import time

import tornado.ioloop


def func():
    print("Runnint task at ", time.time())


p = tornado.ioloop.PeriodicCallback(func, 1000)
print(p, type(p))
p.start()

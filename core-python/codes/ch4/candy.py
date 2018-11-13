import time
from atexit import register
from random import randrange
from threading import Thread, Lock, BoundedSemaphore


lock = Lock()
MAX = 5
candytray = BoundedSemaphore(MAX)


def fill():
    with lock:
        print("filling candy...")
        try:
            candytray.release()
        except ValueError as err:
            print("full, skiping")
        else:
            print("fill OK")


def buy():
    with lock:
        if candytray.acquire(False):
            print("buy OK")
        else:
            print("empty, skipping")


def producer(loops):
    for i in range(loops):
        fill()
        time.sleep(randrange(3))


def consume(loops):
    for i in range(loops):
        buy()
        time.sleep(randrange(3))


def main():
    print("starting at: %s" % time.ctime())
    nloops = randrange(2, 6)
    print("MAX %s" % MAX)
    Thread(target=consume, args=(randrange(nloops, nloops+MAX+2),)).start()
    Thread(target=producer, args=(nloops,)).start()


@register
def _atexit():
    print("all DONE at: %s" % time.ctime())


if __name__ == "__main__":
    main()

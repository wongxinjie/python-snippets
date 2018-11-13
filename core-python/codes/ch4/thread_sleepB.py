import thread
from time import ctime, sleep


loops = [4, 2]


def loop(n, nsec, lock):
    print 'start loop', n, 'at: ', ctime()
    sleep(nsec)
    print 'loop', n, 'done at:', ctime()
    lock.release()


def main():
    print 'starting at: ', ctime()
    locks = []
    nloops = range(len(loops))

    for i in nloops:
        lock = thread.allocate_lock()
        lock.acquire()
        locks.append(lock)

    for i in nloops:
        thread.start_new_thread(loop, (i, loops[i], locks[i]))

    for i in nloops:
        while locks[i].locked():
            pass

    print 'all DONE at: ', ctime()


if __name__ == "__main__":
    main()

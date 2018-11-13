import time
import functools

from worker_thread import WorkerThread


def timeit(func):
    @functools.wraps(func)
    def warpper(*args, **kwargs):
        s = time.time()
        result = func(*args, **kwargs)
        t = (time.time() - s) * 1000
        msg = '%s(%s) takes %s ms' % (func.__name__, ", ".join(map(str, args)), t)
        print(msg)
        return result
    return warpper


# @timeit
def fib(x):
    time.sleep(0.005)
    if x < 2:
        return 1
    return (fib(x - 2) + fib(x - 1))


# @timeit
def fac(x):
    time.sleep(0.1)
    if x < 2:
        return 1
    return x * fac(x - 1)


# @timeit
def sum_(x):
    time.sleep(0.1)
    if x < 2:
        return 1
    return x + sum_(x - 1)


funcs = [fib, fac, sum_]
n = 12


def main():
    nfuncs = range(len(funcs))

    print('***SINGLE THREAD')
    s = time.time()
    for i in nfuncs:
        print(funcs[i](n))
    print('TAKES %s' % (time.time() - s))

    print("*** MULTIPLE THREAD")
    threads = []
    for i in nfuncs:
        t = WorkerThread(funcs[i], (n,), funcs[i].__name__)
        threads.append(t)

    s = time.time()
    for t in threads:
        t.start()

    for t in threads:
        t.join()
        print(t.get_result())
    print('TAKES %s' % (time.time() - s))


if __name__ == "__main__":
    main()

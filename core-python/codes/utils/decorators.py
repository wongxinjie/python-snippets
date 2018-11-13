import time
import functools


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

import gc

gc.set_debug(gc.DEBUG_LEAK)
counter = 0


class A:

    def __init__(self):
        global counter
        c = counter
        a = list()
        for _ in range(10):
            a = [a]
            a.append(a)
        del a
        counter = c + 1

    def __del__(self):
        global counter
        c = counter
        counter = c - 1


for _ in range(10000):
    a = list()
    b = list()
    a.append(b)
    b.append(a)

    del a
    del b
    # gc.collect()

gc.collect()
print(counter)

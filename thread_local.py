import threading

context = threading.local()
context.x = 8


class Context(object):
    x = 10086


ctx = Context()


def f(name, x=None):
    if x is not None:
        context.x = x
        ctx.x = x
    print('name - %s, context.x=%s, ctx.x=%s' % (name, context.x, ctx.x))


def main():
    print(context.x, ctx.x)
    threads = [
        threading.Thread(target=f, args=('thread-1', 10)),
        threading.Thread(target=f, args=('thread-2', 12))
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print(context.x, ctx.x)
main()

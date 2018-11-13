import time
import threading


class WorkerThread(threading.Thread):

    def __init__(self, func, args, name=''):
        super().__init__()
        self.name = name
        self.func = func
        self.args = args
        self.result = None

    def get_result(self):
        return self.result

    def run(self):
        s = time.time()
        self.result = self.func(*self.args)
        print("%s(%s) = %s ==> %s ms" % (self.name, self.args, self.result, (time.time() - s) * 1000))

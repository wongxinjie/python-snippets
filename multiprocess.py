import os
import multiprocessing as mp
from multiprocessing import Pipe

a, b = Pipe()


def func(q):
    print('pid ', os.getpid())
    print('ppid ', os.getppid())
    q.put("hello")


def main_process_func():
    print('main pid ', os.getpid())
    print('main ppid ', os.getppid())
    print(mp.cpu_count())
    print("echo in main func")


def pipe_func_a(msg):
    a.send(msg)
    print('a send msg ', msg)


def pipe_func_b():
    msg = b.recv()
    print('b recv ', msg)


if __name__ == "__main__":
    # q = mp.Queue()
    # p = mp.Process(target=func, args=(q, ))
    # p.start()
    # main_process_func()
    # print(q.get())
    # p.join()
    msg = "Happy New Year"
    pa = mp.Process(target=pipe_func_a, args=(msg, ))
    pb = mp.Process(target=pipe_func_b, args=())
    pa.start()
    pb.start()

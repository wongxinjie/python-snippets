#!/usr/bin/env python
"""
    scheduler.py
    ~~~~~~~~~~~~~~~~~~~~~~~
    
    :author: wongxinjie
    :copyright: (c) 2019, Tungee
    :date created: 2019-03-24 22:25
    :python version: Python3.6
"""
import time
import heapq
from threading import Thread, Lock


class TaskException(Exception):
    pass


class Task:

    def __init__(self, name, run_time, func, args=None, kwargs=None):
        self.name = name
        self.run_time = run_time
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def __repr__(self):
        return "Task - %s" % self.name


class Scheduler:

    def __init__(self):
        self.time_task_heap = list()
        self.entry_dict = dict()
        self.lock = Lock()

    def add_task(self, task):
        self.lock.acquire()
        if task.name in self.entry_dict:
            raise TaskException("task name already exists!")

        thread = Thread(
            target=task.func, name=task.name,
            args=task.args, kwargs=task.kwargs
        )
        entry = (task.run_time, thread)
        self.time_task_heap.append(entry)
        heapq.heapify(self.time_task_heap)

        self.entry_dict[thread.name] = entry

        self.lock.release()
        print("add task success")

    def cancel_task(self, name):
        self.lock.acquire()
        if name not in self.entry_dict:
            raise TaskException("task not exists")

        entry = self.entry_dict.pop(name)
        self.time_task_heap.remove(entry)
        heapq.heapify(self.time_task_heap)

        self.lock.release()

    def dispatch(self):
        while True:
            self.lock.acquire()
            if not self.time_task_heap:
                self.lock.release()
                time.sleep(0.1)
                continue

            entry = self.time_task_heap[0]
            run_time, thread = entry
            if run_time <= time.time():
                thread.run()
                self.time_task_heap.remove(entry)
                self.entry_dict.pop(thread.name)
                self.lock.release()
            else:
                self.lock.release()
                time.sleep(run_time - time.time())

    def run(self):
        dispatcher = Thread(target=self.dispatch)
        dispatcher.run()
        # dispatcher.join()


def demo(x):
    print("%s x = %s" % (time.time(), x))


if __name__ == "__main__":
    t = Task("demo", time.time() + 2, demo, (2,))
    s = Scheduler()
    s.add_task(t)
    s.run()

    print('hear')
    t = Task("task - 2", time.time() + 1, demo, (4,))
    s.add_task(t)

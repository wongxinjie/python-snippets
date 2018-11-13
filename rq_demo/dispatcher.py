# coding: utf-8
from rq import Queue
from redis import Redis

from workers import (
    fast_worker,
    lazy_worker
)

rdb = Redis()

fast_queue = Queue('fast', connection=rdb)
lazy_queue = Queue('lazy', connection=rdb)


if __name__ == "__main__":
    short_tasks = [1, 3, 2, 5, 6, 7, 8]
    long_tasks = [20, 12, 34, 56, 70, 87]

    for task in short_tasks:
        fast_queue.enqueue(fast_worker, task)

    for task in long_tasks:
        lazy_queue.enqueue(lazy_worker, task)

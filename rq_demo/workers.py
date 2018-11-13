# coding: utf-8
import time


def fast_worker(interval):
    print('fast_worker working and sleep for {}s'.format(interval))
    time.sleep(interval)


def lazy_worker(interval):
    print('lazy_worker workering and sleep for {}s'.format(interval))
    time.sleep(interval)

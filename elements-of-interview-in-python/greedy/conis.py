#!/usr/bin/env python
"""
    conis.py
    ~~~~~~~~~~~~~~~~~~~~~~~
    
    :author: wongxinjie
    :copyright: (c) 2019, Tungee
    :date created: 2019-03-24 18:01
    :python version: Python3.6
"""


def change_making(cents):
    coins = [100, 50, 25, 10, 5, 1]
    num_coins = 0
    for c in coins:
        num_coins += int(cents / c)
        cents %= c

    return num_coins


if __name__ == "__main__":
    n = change_making(17)
    print(n)


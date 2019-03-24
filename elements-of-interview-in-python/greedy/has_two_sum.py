#!/usr/bin/env python
"""
    has_two_sum.py
    ~~~~~~~~~~~~~~~~~~~~~~~
    
    :author: wongxinjie
    :copyright: (c) 2019, Tungee
    :date created: 2019-03-24 18:14
    :python version: Python3.6
"""


def has_two_sum(A, t):
    i, j = 0, len(A) - 1
    while i <= j:
        if A[i] + A[j] == t:
            return True
        elif A[i] + A[j] < t:
            i += 1
        else:
            j -= 1

    return False


if __name__ == "__main__":
    A = [-2, -1, 2, 4, 7, 11]
    assert has_two_sum(A, 6)
    assert has_two_sum(A, 10)
    assert not has_two_sum(A, 7)
    assert has_two_sum(A, 13)

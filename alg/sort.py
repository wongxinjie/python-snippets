import random


def bubble_sort(A):
    size = len(A)
    sort_ready = False
    for n in range(size):
        for m in range(size - n - 1):
            if A[m] < A[m+1]:
                A[m], A[m+1] = A[m+1], A[m]
            else:
                sort_ready = True
        if sort_ready:
            break


A = list(range(10))
random.shuffle(A)
print(A)
bubble_sort(A)
print(A)

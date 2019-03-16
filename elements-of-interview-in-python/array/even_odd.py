def even_odd(A):
    next_even, next_odd = 0, len(A) - 1
    while next_even < next_odd:
        if A[next_even] % 2 == 0:
            next_even += 1
        else:
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd -= 1


if __name__ == "__main__":
    a = [2, 1, 3, 7, 4, 8, 9, 12]
    even_odd(a)
    print(a)

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_index, A):
    pivot = A[pivot_index]

    # First pass: group elements smaller than pivot
    for i in range(len(A)):
        for k in range(i + 1, len(A)):
            if A[k] < pivot:
                A[i], A[k] = A[k], A[i]
                break

    for i in reversed(range(len(A))):
        if A[i] < pivot:
            break

        for k in reversed(range(i)):
            if A[k] > pivot:
                A[i], A[k] = A[k], A[i]
                break


A = [0, 1, 2, 0, 2, 1, 1]
dutch_flag_partition(3, A)
print(A)

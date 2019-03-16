def intersect_two_sorted_arrays(A, B):
    x, y, intersection_A_B = 0, 0, []
    while x < len(A) and y < len(B):
        if A[x] == B[y]:
            if x == 0 or A[x] != A[x-1]:
                intersection_A_B.append(A[x])
            x, y = x + 1, y + 1
        elif A[x] < B[y]:
            x += 1
        else:
            y += 1
    return intersection_A_B


print(intersect_two_sorted_arrays([2, 3, 3, 5, 7, 11], [3, 4, 7, 15, 31]))

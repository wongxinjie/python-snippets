def search_first_of_k(A, k):
    left, right, result = 0, len(A) - 1, -1
    while left <= right:
        mid = (left + right) // 2
        if A[mid] > k:
            right = mid - 1
        elif A[mid] == k:
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result


if __name__ == "__main__":
    A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
    assert search_first_of_k(A, 108) == 3

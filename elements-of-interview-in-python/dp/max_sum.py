import itertools


def find_maximum_subarray(A):
    min_sum, max_mun = 0, 0
    for running_sum in itertools.accumulate(A):
        min_sum = min(min_sum, running_sum)
        max_mun = max(max_mun, running_sum - min_sum)
    return max_mun


def find_maximum_subarray_n_space(A):
    cache = [0] * len(A)
    for idx, n in enumerate(A):
        if idx == 0:
            cache[idx] = n
        else:
            cache[idx] = cache[idx - 1] + n

    max_sum = cache[0]
    for n in cache[1:]:
        if n > max_sum:
            max_sum = n
    return max_sum


if __name__ == "__main__":
    A = [904, 40, 523, 12, -335, -385, -124, 481, -31]
    print(find_maximum_subarray(A))
    print(find_maximum_subarray_n_space(A))

def fibonacci(n, cache=None):
    if cache is None:
        cache = {}

    if n <= 1:
        return n
    elif n not in cache:
        cache[n] = fibonacci(n-1, cache) + fibonacci(n-2, cache)
    return cache[n]


def fib2(n):
    if n <= 1:
        return n

    prev_2, prev_1 = 0, 1
    for _ in range(1, n):
        current = prev_1 + prev_2
        prev_2, prev_1 = prev_1, current
    return prev_1


print(fib2(100))

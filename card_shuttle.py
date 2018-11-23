import random


def shuffle(array):
    size = len(array)

    for idx in range(size - 1, -1, -1):
        i = random.randint(0, idx)
        array[idx], array[i] = array[i], array[idx]

    return array


cards = [i for i in range(1, 55)]
print(cards)
print(shuffle(cards))

import math


def generate_power_set(S):
    power_set = []

    for int_for_subset in range(1 << len(S)):
        bit_array = int_for_subset
        subset = []
        while bit_array:
            subset.append(int(math.log(bit_array & ~(bit_array - 1), 2)))
            bit_array &= bit_array - 1
        power_set.append(subset)

    return power_set


print(generate_power_set([0, 1, 2]))

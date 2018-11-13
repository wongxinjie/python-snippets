def count_bits(x):
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1
    return num_bits


# The parity of a binary word is 1 if the number of 1s in the word is odd; otherwise, it is 0.
# For example, the parity of 1011 is 1, and the parity of 10001000 is 0.

# O(n)
def parity_brute_force(x):
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result


# O(k)
def parity_drop_lowest_bit(x):
    result = 0
    while x:
        result ^= 1
        x &= (x - 1)
    return result


# O(log n)
def parity_xor(x):
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1


# Right propagate the rightmost set bit in x, e.g., turns (01010000)2 to (01011111)2.
def right_progate_set_bit(x):
    zero_bits = 0
    shift_x = x
    while shift_x:
        if shift_x & 1:
            break
        else:
            zero_bits += 1
            shift_x >>= 1

    y = 2 ** zero_bits - 1
    return x | y


# Compute x modulo a power of two, e.g., returns 13 for 77 mod 64.
def compute_modulo(x):
    max_power_of_two = 1
    while max_power_of_two < x:
        max_power_of_two <<= 1
    max_power_of_two >>= 1

    return x ^ max_power_of_two


# Test if x is a power of 2, i.e., evaluates to true for x = 1,2,4,8,..., false for all other value
def is_powwer_of_two(x):
    num_bits = 0
    while x:
        if x & 1:
            if num_bits:
                return False
            num_bits += 1
        x >>= 1
    return True


# given an integer
def integer_to_ip(x):
    segs = []
    while x:
        seg = int(x % 256)
        segs.append(str(seg))
        x = int(x / 256)
    segs.reverse()
    return ".".join(segs)


print(integer_to_ip(0x11345678))

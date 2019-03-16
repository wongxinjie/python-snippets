import string
import functools


def is_palindromic(s):
    return all(s[i] == s[~i] for i in range(len(s) // 2))


def construct_from_base(num_as_int, base):
    if num_as_int == 0:
        return ''

    rv = construct_from_base(num_as_int // base, base)
    rv += string.hexdigits[num_as_int % base].upper()
    return rv


def convert_base(num_as_string, org_base, dest_base):
    is_negative = num_as_string[0] == '-'
    num_as_int = functools.reduce(
        lambda x, c: x * org_base + string.hexdigits.index(c.lower()),
        num_as_string[is_negative:], 0
    )
    return ('-' if is_negative else '') + (
        '0' if num_as_int == 0 else construct_from_base(num_as_int, dest_base))


print(convert_base('1AA', 16, 10))

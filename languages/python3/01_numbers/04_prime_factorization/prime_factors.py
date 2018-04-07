#!/usr/bin/python3


def prime_factor_brute(x):
    if type(x) is not int:
        if hasattr(x, 'is_integer') and not x.is_integer():
            raise ValueError('Expected integer argument, received {}'
                             .format(x))
        try:
            x = int(x)
        except ValueError:
            raise ValueError('Expected integer argument, received {}'
                             .format(x))

    if x == 1:
        return []
    for i in range(2, x):
        if x % i == 0:
            return [i] + prime_factor_brute(int(x / i))
    return [x]

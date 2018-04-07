import math
from decimal import *


def fibonacci_recursive(n):
    if n < 0:
        raise ValueError('Provide n >= 0. n:{}'.format(n))
    if n < 2:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_iterative(n):
    if n < 0:
        raise ValueError('Provide n >= 0. n:{}'.format(n))
    if n < 2:
        return n
    a = 0
    b = 1
    c = 0
    for i in range(n - 1):
        c = a + b
        a = b
        b = c
    return c


def fibonacci_doubling(n):
    # Algorithm Source: https://www.nayuki.io/page/fast-fibonacci-algorithms
    if n < 0:
        raise ValueError('Provide n >= 0. n:{}'.format(n))
    if n < 2:
        return n
    k = 1
    fk = 1
    fk1 = 1
    while k * 2 < n:
        k = k * 2
        f2k = fk * (2 * fk1 - fk)
        f2k1 = fk1 ** 2 + fk ** 2
        fk = f2k
        fk1 = f2k1
    while k < n:
        c = fk + fk1
        fk = fk1
        fk1 = c
        k += 1
    return fk

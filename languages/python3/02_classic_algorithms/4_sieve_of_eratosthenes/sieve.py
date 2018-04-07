import math


def sieve(n):
    """Return all primes p such that p <= n"""
    if n < 2:
        raise ValueError('Provide n >= 2. n:{}'.format(n))
    a = [False, False] + [True] * (n - 1)
    for i in range(2, int(math.sqrt(n)) + 1):
        if a[i]:
            j = i ** 2
            while j <= n:
                a[j] = False;
                j += i
    return [i for i in range(n + 1) if a[i]]

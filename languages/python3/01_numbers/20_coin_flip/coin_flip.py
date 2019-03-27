import random


def coin_flip(n):
    flips = []
    for i in range(n):
        if random.randint(0, 1):
            flips.append('H')
        else:
            flips.append('T')
    return flips

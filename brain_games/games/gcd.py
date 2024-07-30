# Логика игры.
import random


RULES = 'Find the greatest common divisor of given numbers.'


def logic():
    n = []
    n.append(str(random.randint(1, 100)))
    n.append(str(random.randint(1, 100)))
    a = int(n[0])
    b = int(n[1])
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return (" ".join(n), max(a, b))

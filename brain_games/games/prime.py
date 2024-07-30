# Логика игры.
import random


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def logic():
    n = random.randint(1, 100)
    for i in range(2, int(n * 0.5) + 1):
        if n % i == 0:
            return (n, 'no')
        else:
            continue
    else:
        return (n, 'yes')

# Логика игры.
import random


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def logic():
    n = random.randint(1, 100)
    if n % 2 == 0:
        return (n, 'yes')
    else:
        return (n, 'no')

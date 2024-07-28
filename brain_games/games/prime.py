# Логика игры
import random


def prime() -> str:
    n = random.randint(1, 100)
    print('Question:', n)
    for i in range(2, int(n * 0.5) + 1):
        if n % i == 0:
            return 'no'
        else:
            continue
    else:
        return 'yes'

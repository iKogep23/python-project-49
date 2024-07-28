# Логика игры
import random


def even() -> str:
    n = random.randint(1, 100)
    print('Question:', n)
    if n % 2 == 0:
        return 'yes'
    else:
        return 'no'

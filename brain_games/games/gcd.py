# Логика игры
import random


def gcd() -> int:
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    print(f'Question: {a} {b}')
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return max(a, b)

# Логика игры
import random


def progression():
    p = []
    start = random.randint(0, 100)
    step = random.randint(1, 10)
    i = random.randrange(9)
    for x in range(start, start + step * 10, step):
        p.append(str(x))
    result = p[i]
    p[i] = '..'
    print(f'Question: {" ".join(p)}')
    return result

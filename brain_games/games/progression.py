import random


RULES = 'What number is missing in the progression?'


def play_game():
    '''Return a progression and one missing element of this progression.'''
    p = []
    start = random.randint(0, 100)
    step = random.randint(1, 10)
    i = random.randrange(9)
    for x in range(start, start + step * 10, step):
        p.append(str(x))
    result = p[i]
    p[i] = '..'
    return (" ".join(p), result)

import random


RULES = 'Find the greatest common divisor of given numbers.'


def gcd(a: int, b: int):
    '''Return the greatest common divisor of two numbers.'''
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return max(a, b)


def play_game():
    '''Return two numbers and greatest common divisor.'''
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    return (f'{a} {b}', gcd(a, b))

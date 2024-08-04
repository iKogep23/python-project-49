import random


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(n):
    '''Checking whether a given number is even or odd.'''
    return n % 2 == 0


def play_game():
    '''Return a random number and correct answer.'''
    n = random.randint(1, 100)
    return (n, 'yes') if is_even(n) else (n, 'no')

import random


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n: int):
    '''Check if given number is prime or not.'''
    if n == 1:
        return False
    for i in range(2, int(n * 0.5) + 1):
        if n % i == 0:
            return False
    else:
        return True


def play_game():
    '''Return random number and correct answer.'''
    n = random.randint(1, 100)
    return (n, 'yes') if is_prime(n) else (n, 'no')

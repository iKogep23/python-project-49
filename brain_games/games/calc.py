import random


RULES = 'What is the result of the expression?'


def calculation(a, operand, b):
    '''Returns the result of the expression.'''
    match operand:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b


def play_game():
    '''Returns the expression and result.'''
    a = random.randint(1, 100)
    operands = ['+', '-', '*']
    operand = random.choice(operands)
    b = random.randint(1, 100)
    return (f'{a} {operand} {b}', calculation(a, operand, b))

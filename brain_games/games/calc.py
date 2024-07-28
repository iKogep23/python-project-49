# Логика игры
import random


def calc() -> str:
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    operands = ['+', '-', '*']
    operand = random.choice(operands)
    match operand:
        case '+':
            print(f'Question: {a} + {b}')
            result = a + b
        case '-':
            print(f'Question: {a} - {b}')
            result = a - b
        case '*':
            print(f'Question: {a} * {b}')
            result = a * b
    return result

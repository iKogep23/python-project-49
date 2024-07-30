# Логика игры.
import random


RULES = 'What is the result of the expression?'


def logic():
    n = []
    n.append(str(random.randint(1, 100)))
    operands = ['+', '-', '*']
    n.append(random.choice(operands))
    n.append(str(random.randint(1, 100)))
    a = int(n[0])
    b = int(n[2])
    match n[1]:
        case '+':
            return (" ".join(n), a + b)
        case '-':
            return (" ".join(n), a - b)
        case '*':
            return (" ".join(n), a * b)

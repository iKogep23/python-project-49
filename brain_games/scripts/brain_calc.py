import random
import prompt
from brain_games.cli import welcome_user


def question() -> str:
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    operands = ['+', '-', '*']
    operand = random.choice(operands)
    match operand:
        case '+':
            print(f'Question: {a} + {b}')
            c = a + b
        case '-':
            print(f'Question: {a} - {b}')
            c = a - b
        case '*':
            print(f'Question: {a} * {b}')
            c = a * b
    answer = prompt.string('Your answer: ')
    if answer == str(c):
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{c}'.")
        return False


def main():
    name = welcome_user()
    print('What is the result of the expression?')
    for _ in range(3):
        answer = question()
        if answer is True:
            print('Correct!')
        else:
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()

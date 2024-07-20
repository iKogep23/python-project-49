import random
import prompt
from brain_games.cli import welcome_user


def progression():
    p = []
    start = random.randint(0, 100)
    step = random.randint(1, 10)
    for x in range(start, start + step * 10, step):
        p.append(x)
    return p


def question() -> str:
    p = progression()
    i = random.randrange(9)
    n = p[i]
    p[i] = '..'
    print(f'Question: {p}')
    answer = prompt.string('Your answer: ')
    if answer == str(n):
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{n}'.")
        return False


def main():
    name = welcome_user()
    print('What number is missing in the progression?')
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

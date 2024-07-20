import random
import prompt
from brain_games.cli import welcome_user


def gcd(a, b) -> int:
    if a == 0 or b == 0:
        return max(a, b)
    return gcd(b, a % b)


def question() -> str:
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    print(f'Question: {a} {b}')
    answer = prompt.string('Your answer: ')
    c = gcd(a, b)
    if answer == str(c):
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{c}'.")
        return False


def main():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
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

import random
import prompt
from brain_games.cli import welcome_user


def question(n: int) -> str:
    print('Question:', n)
    answer = prompt.string('Your answer: ').lower()
    if n % 2 == 0:
        if answer == 'yes':
            return True
        else:
            print("'no' is wrong answer ;(. Correct answer was 'yes'.")
            return False
    else:
        if answer == 'no':
            return True
        else:
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            return False


def main():
    name = welcome_user()
    print('Answer "yes" if number is even, otherwise answer "no".')
    for _ in range(3):
        n = random.randint(1, 100)
        answer = question(n)
        if answer is True:
            print('Correct!')
        else:
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()

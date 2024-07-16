import random
import prompt
from brain_games.cli import welcome_user


def even(n: int) -> str:
    print('Question:', n)
    answer = prompt.string('Your answer: ')
    return answer


def main():
    name = welcome_user()
    print('Answer "yes" if number is even, otherwise answer "no".')
    for _ in range(3):
        n = random.randint()
        answer = even(n)
        if n % 2 == 0:
            if answer == 'yes':
                print('Correct!')
            else:
                print("'no' is wrong answer ;(. Correct answer was 'yes'.")
                print(f"Let's try again, {name}!")
                break
        if n % 2 != 0:
            if answer == 'no':
                print('Correct!')
            else:
                print("'no' is wrong answer ;(. Correct answer was 'yes'.")
                print(f"Let's try again, {name}!")
                break
    else:
        print(f'Congratulations, {name}')


if __name__ == '__main__':
    main()

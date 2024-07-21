import random
import prompt
from brain_games.cli import welcome_user


def question(n: int) -> str:
    print('Question:', n)
    answer = prompt.string('Your answer: ').lower()
    for i in range(2, int(n * 0.5) + 1):
        if n % i == 0:
            if answer.lower() == 'no':
                return True
            else:
                print("'yes' is wrong answer ;(. Correct answer was 'no'.")
                return False
    else:
        if answer.lower() == 'yes':
            return True
        else:
            print("'no' is wrong answer ;(. Correct answer was 'yes'.")
            return False


def main():
    name = welcome_user()
    print('Answer "yes" if number number is prime. Otherwise answer "no".')
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

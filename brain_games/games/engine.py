# Управление процессом игры
import prompt


def engine(game, name):
    for _ in range(3):
        res = game()
        answer = prompt.string('Your answer: ').lower()
        if str(res) == answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{res}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')

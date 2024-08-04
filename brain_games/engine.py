import prompt
from brain_games.cli import welcome_user


def control(game):
    '''Controls all game processes.'''
    name = welcome_user()
    print(game.RULES)
    for _ in range(3):
        res = game.play_game()
        print('Question:', res[0])
        answer = prompt.string('Your answer: ')
        if str(res[1]) == answer.lower():
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{res[1]}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
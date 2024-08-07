import prompt
from brain_games.cli import welcome_user


def control(game):
    '''Controls all game processes.'''
    name = welcome_user()
    print(game.RULES)
    for _ in range(3):
        q, result = game.play_game()
        print('Question:', q)
        answer = prompt.string('Your answer: ')
        if str(result) == answer.lower():
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{result}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')

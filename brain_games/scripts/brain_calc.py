# Вывод на экран приветствия, правил и запуск игры.
from brain_games.cli import welcome_user
from brain_games.games.engine import engine
from brain_games.games.calc import calc


def main():
    name = welcome_user()
    print('What is the result of the expression?')
    engine(calc, name)

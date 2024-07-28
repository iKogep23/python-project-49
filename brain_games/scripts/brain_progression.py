# Вывод на экран приветствия, правил и запуск игры.
from brain_games.cli import welcome_user
from brain_games.games.engine import engine
from brain_games.games.progression import progression


def main():
    name = welcome_user()
    print('What number is missing in the progression')
    engine(progression, name)

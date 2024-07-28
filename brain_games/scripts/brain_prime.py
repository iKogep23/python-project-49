# Вывод на экран приветствия, правил и запуск игры.
from brain_games.cli import welcome_user
from brain_games.games.engine import engine
from brain_games.games.prime import prime


def main():
    name = welcome_user()
    print('Answer "yes" if the number is prime. Otherwise answer "no".')
    engine(prime, name)

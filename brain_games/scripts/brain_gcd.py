# Вывод на экран приветствия, правил и запуск игры.
from brain_games.cli import welcome_user
from brain_games.games.engine import engine
from brain_games.games.gcd import gcd


def main():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    engine(gcd, name)

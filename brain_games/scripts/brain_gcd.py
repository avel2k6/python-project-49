#!/usr/bin/env python3
from brain_games import cli
from brain_games.games import gcd
from brain_games import game


def main():
    cli.welcome_user()
    game.run(gcd.QUESTION, gcd.get_game_data)


if __name__ == '__main__':
    main()

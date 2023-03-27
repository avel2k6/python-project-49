#!/usr/bin/env python3
from brain_games.games import even
from brain_games import game


def main():
    game.run(even.QUESTION, even.get_game_data)


if __name__ == '__main__':
    main()

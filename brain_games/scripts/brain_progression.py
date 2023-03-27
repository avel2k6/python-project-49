#!/usr/bin/env python3
from brain_games.games import progression
from brain_games import game


def main():
    game.run(progression.QUESTION, progression.get_game_data)


if __name__ == '__main__':
    main()

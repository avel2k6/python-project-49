import random

QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return True if (number % 2 == 0) else False


def get_game_data():
    random_int = random.randint(0, 1000)
    answer = 'yes' if is_even(random_int) else 'no'
    return [random_int, answer]

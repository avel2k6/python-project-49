import random

QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MAX_NUMBER = 10


def is_prime(number):
    if (number < 2):
        return False
    divider = 2
    MAX_DIVIDER = number / 2
    while (divider <= MAX_DIVIDER):
        if (number % divider == 0):
            return False
        divider += 1
    return True


def get_game_data():
    random_int = random.randint(0, MAX_NUMBER)
    answer = 'yes' if is_prime(random_int) else 'no'
    return [random_int, answer]

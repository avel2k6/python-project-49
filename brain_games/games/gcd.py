import random

QUESTION = 'Find the greatest common divisor of given numbers.'
MAX_RANDOM_NUMBER = 10


def gcd(n1, n2):
    if (n1 == 0 or n2 == 0):
        return n1 + n2
    return gcd(max([n1, n2]) % min([n1, n2]), min([n1, n2]))


def get_game_data():
    first_random_number = random.randint(0, MAX_RANDOM_NUMBER)
    second_random_number = random.randint(0, MAX_RANDOM_NUMBER)
    question = f'{first_random_number} {second_random_number}'
    answer = str(gcd(first_random_number, second_random_number))
    return [question, answer]

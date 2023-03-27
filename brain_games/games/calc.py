import random

QUESTION = 'What is the result of the expression?'
MAX_RANDOM_NUMBER = 100


def get_game_data():
    operations = ['+', '-', '*']
    operation_index = random.randint(0, len(operations) - 1)
    current_operation = operations[operation_index]
    first_random_number = random.randint(0, MAX_RANDOM_NUMBER)
    second_random_number = random.randint(0, MAX_RANDOM_NUMBER)
    match current_operation:
        case '+':
            game_question = f'{first_random_number} + {second_random_number}'
            answer = first_random_number + second_random_number
            return [game_question, str(answer)]
        case '-':
            game_question = f'{first_random_number} - {second_random_number}'
            answer = first_random_number - second_random_number
            return [game_question, str(answer)]
        case '*':
            game_question = f'{first_random_number} * {second_random_number}'
            answer = first_random_number * second_random_number
            return [game_question, str(answer)]
        case _:
            raise ValueError('undefined operation')

import random

QUESTION = 'What number is missing in the progression?'


MIN_PROGRESSION_NUMBER = 6
MAX_PROGRESSION_STEP = 4


def generate_progression(min_step):
    current_step = 0
    max_step_count = min_step + random.randint(1, 10)
    current_number = random.randint(0, MAX_PROGRESSION_STEP)
    step = random.randint(0, MAX_PROGRESSION_STEP)
    progression = [f'{current_number}']
    while (current_step < max_step_count):
        current_number = step + current_number
        progression.append(f'{current_number}')
        current_step += 1
    return progression


def get_game_data():
    progression = generate_progression(MIN_PROGRESSION_NUMBER)
    secret_number_id = random.randint(0, len(progression) - 1)
    answer = f'{progression[secret_number_id]}'
    progression[secret_number_id] = '..'
    question = ' '.join(progression)
    return [question, answer]

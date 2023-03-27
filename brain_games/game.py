import prompt

MAX_TRY_COUNT = 3


def run_game_round(get_game_data):
    [question_value, answer] = get_game_data()
    print(f'Question: {question_value}')
    user_answer = prompt.string('Your answer:')
    if (user_answer == answer):
        print('Correct!')
        return True
    else:
        print(f'\'{user_answer}\' is wrong answer ;(.',
              f'Correct answer was \'{answer}\'.')
        return False


def run(question, get_game_data):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(question)
    current_try_number = 1
    while (current_try_number <= 3):
        is_success = run_game_round(get_game_data)
        if (is_success):
            current_try_number += 1
        else:
            return
    print(f'Congratulations, {name}!')

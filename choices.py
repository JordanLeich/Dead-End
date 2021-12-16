from other.colors import print_sleep


def error_message(choices, audio_opt=0):  # sanitize options displayed for users
    if choices[-1] == 'unlock_all_cheat':  # remove cheat code 
        print(f'Error choice must be one of: {", ".join(choices[:-1])}\n')
    elif audio_opt:  # remove audio large string of choices
        print(f'Error choice must be: (1-100) or {", ".join(choices[-audio_opt:])}\n')
    else:
        print(f'Error choice must be one of: {", ".join(choices)}\n')


# helper function for player choices - handling errors and what paths to take next
def _player_choice(choices, choice_options: list, audio_opt=0, user_input=' ') -> str:
    while user_input.lower() not in choices:
        user_input = str(input('\n'.join(choice_options)))
        from game import sounds
        sounds.menu_button_sound()
        print_sleep('', 1)
        if user_input.lower() not in choices:
            error_message(choices, audio_opt)
        else:
            return user_input.lower()

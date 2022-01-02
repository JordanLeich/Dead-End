""" This file is used to control cheats and how the game functions in a specific order based on user input. """
from chapters.chapter1 import Chapter1
from chapters.chapter2 import Chapter2
from chapters.chapter3 import Chapter3

from choices import _player_choice
from other.colors import print_green, print_sleep, print_yellow, print_red
from game import player1, sounds, game_data, Difficulty
from random import randint


# GAME SETUP, PROCESS, AND RESET HANDLERS

def load_or_save_data():
    """loads or saves data from the data.json game data file"""
    player1.load_data(game_data.load_game())


def unlock_all_cheat():
    """secret cheat code that activates unlimited money, health, and in game items"""
    sounds.good_luck()
    player1.reset_values(999999, 999999, True)
    player1.difficulty = Difficulty(0)
    print_green('All cheats have been activated!\n', 2)
    player1.checkpoint_save()


def infinite_health_cheat():
    """secret cheat code that activates unlimited health"""
    sounds.good_luck()
    player1.health = 999999
    player1.difficulty = Difficulty(0)
    print_green('Infinite health cheat has been activated!\n', 2)
    player1.checkpoint_save()


def infinite_money_cheat():
    """secret cheat code that activates unlimited money"""
    sounds.good_luck()
    player1.balance = 999999
    player1.health = 200  # health has to be set to an amount above at least 0.
    # otherwise, the player will be given 0 health and the game will instantly end.
    player1.difficulty = Difficulty(0)
    print_green('Infinite money cheat has been activated!\n', 2)
    player1.checkpoint_save()


# helper function for player health setting and printing
def _difficulty_set_health():
    if player1.difficulty == Difficulty(1):
        player1.health = 200
    elif player1.difficulty == Difficulty(2):
        player1.health = 100
    elif player1.difficulty == Difficulty(3):
        player1.health = 50
    elif player1.difficulty == Difficulty(0):
        unlock_all_cheat()
    else:
        print('Since a saved difficulty value could not be found...')
        player1.health = 100
    print_health(player1.difficulty,
                 f'{player1.difficulty.name} mode has been selected, you will begin with {player1.health} health.\n',
                 1)


def game():
    """Simply plays the beginning of chapter 1."""
    Chapter1().game()


def xp_level_system():
    """Used for leveling and award the player with their respective XP amount based their difficulty level."""
    # player is awarded XP
    if player1.xp_amount < 1000:  # set to 1000 since lvl 10 is achieved at xp amount 1001 and above
        initial_xp = player1.xp_amount
        if player1.difficulty == Difficulty(1):
            player1.xp_amount += randint(15, 60)
        elif player1.difficulty == Difficulty(2):
            player1.xp_amount += randint(35, 75)
        elif player1.difficulty == Difficulty(3):
            player1.xp_amount += randint(75, 100)
        elif player1.difficulty == Difficulty(0):  # Cheater difficulty will always receive a flat amount of 500 XP.
            player1.xp_amount = 500
        else:
            player1.xp_amount += randint(1, 100)
        print_green(f'XP gained - {player1.xp_amount - initial_xp}')
    # Leveling the player up
    if player1.xp_amount >= 1000:
        print_green('Reached Maximum XP level - 10\n', 1.5)
        player1.user_level = 10
        player1.print_achievement(('4', 'Rare'))
        return
    elif player1.xp_amount <= 0:
        print_yellow('You currently do not have any XP Level - 0\n', 1)
        player1.user_level = 0
        return
    else:
        player1.user_level = int(player1.xp_amount / 100)
    sounds.good_luck()
    print_green(f'Current XP Amount - {player1.xp_amount}')
    print_green(f'Current XP Level - {player1.user_level}\n', 2)
    return


def difficulty():
    """handles difficulty activation procedure, if a difficulty has not been set then the user will select one"""
    if player1.difficulty.value != -1:
        sounds.difficulty_select_sound()
        print_sleep(f'Current difficulty is set to {player1.difficulty.name}\n', 1)
        print_sleep('Difficulty selection was skipped due to saved difficulty data already existing...\n', 1)

        if player1.check_point == "6":
            choice_options = ['Since you have completed Chapter 1 with your saved data, would you like to '
                              'replay Chapter 1 or continue to Chapter 2 (replay / continue): ']
            choice = _player_choice(['r', 'replay', 'c', 'chapter 2', 'continue', 'chapter2', 'chapter1', 'chapter 1'],
                                    choice_options)
            if choice.lower() in ['c', 'continue', 'chapter2', 'chapter 2']:
                print_yellow('You will now begin Chapter 2.\n', 2)
                Chapter2.game()
            elif choice.lower() in ['r', 'replay', 'chapter1', 'chapter 1']:
                print_yellow('You will now replay Chapter 1.\n', 2)
                Chapter1.game()
        else:
            choice_options = ['Would you like to start a new game or continue with your saved data (new / continue): ']
            choice = _player_choice(['n', 'new', 'c', 'continue'], choice_options)

            if choice in ['n', 'new']:
                player1.reset_values(0, 100, False)
                difficulty_select()
                player1.checkpoint_save('0')
            elif choice in ['c', 'continue']:
                print_green('Continuing game...\n', 1)
            go_to_checkpoint()
    else:
        difficulty_select()


def difficulty_select():
    """allows the user to select a difficulty"""
    print_sleep('--- All difficulty levels ---\n')
    print_green('(1) Easy - Lowest amount of XP awarded\n')
    print_yellow('(2) Medium - Average amount of XP awarded\n')
    print_red('(3) Hardcore - Largest amount of XP awarded\n')
    choices = [str(x) for x in range(1, 4)]
    choices.append('unlock_all_cheat')
    choice_options = ['Select a difficulty: ']
    player1.difficulty = Difficulty(int(_player_choice(choices, choice_options)))
    sounds.difficulty_select_sound()
    _difficulty_set_health()


def go_to_checkpoint():
    """runs movement to levels -- checkpoint when leaving area"""
    story = {1: Chapter1,
             2: Chapter2,
             3: Chapter3,
             }
    if player1.chapter not in story:
        print('Sorry, there is no recent checkpoint for you to go to')
        return
    while 'exit' not in player1.check_point:
        chapter_checkpoints = story[player1.chapter]().checkpoints()  # TODO: Fix crash error here
        if 'bad' in player1.check_point:
            chapter_checkpoints[len(chapter_checkpoints) - 1]()
        else:
            chapter_checkpoints[player1.check_point]()


# move to player class
def print_health(player_difficulty, message, sleep_duration=0):
    """prints the users health and color based upon difficulty selection"""
    if player_difficulty == Difficulty(1):
        print_green(message, sleep_duration)
    elif player_difficulty == Difficulty(2):
        print_yellow(message, sleep_duration)
    elif player_difficulty == Difficulty(3):
        print_red(message, sleep_duration)

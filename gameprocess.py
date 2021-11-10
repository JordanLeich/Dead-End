# from classes import Player, Difficulty
import chapters.chapter2
import game
from game import player1, sounds, game_data, Difficulty
from choices import _player_choice
from chapters.chapter1 import *


# GAME SETUP, PROCESS, AND RESET HANDLERS

def load_or_save_data():
    player1.load_data(game_data.load_game())


def game_intro():
    sounds.intro_sound()
    print_s('''This is a zombie survival game where you must make the best decisions possible in order to live.
As a survivor, you will encounter zombies, weapons, people, and a merchant to buy from with an
in-game currency. Every decision you make has a cause and effect while some lead you to fortune and others will 
lead you to death.\n''', 2.5)
    difficulty()


def unlock_all_cheat():
    sounds.good_luck()
    player1.reset_values(999999, 999999, True)
    player1.difficulty = Difficulty(0)
    print_green('All cheats have been activated!\n', 2)
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


def difficulty():
    if player1.difficulty.value != -1:
        sounds.difficulty_select_sound()
        print_green(f'Current difficulty is {player1.difficulty.name}\n')
        print_green('Difficulty selection was skipped due to saved data already existing...\n', 1)

        if player1.check_point == "6":
            print_yellow('Due to having the end of the Chapter 1 checkpoint, you will now begin Chapter 2.\n', 2)
            chapters.chapter2.start()
        else:
            choice_options = ['Would you like to start a new game or continue with your saved data (new / continue): ']
            choice = _player_choice(['n', 'new', 'c', 'continue'], choice_options)

            if choice in ['n', 'new']:
                player1.reset_values(0, 100, False)
                difficulty_select()
                player1.checkpoint_save()
            elif choice in ['c', 'continue']:
                print_green('Continuing game...\n', 1)
                go_to_checkpoint()
    else:
        difficulty_select()


def difficulty_select():
    print_green('Please select a difficulty level\n')
    print_green('(1) Easy\n')
    print_yellow('(2) Medium\n')
    print_red('(3) Hardcore\n')
    choices = [str(x) for x in range(1, 4)]
    choices.append('unlock_all_cheat')
    choice_options = ['Select a difficulty: ']
    try:
        player1.difficulty = Difficulty(int(_player_choice(choices, choice_options)))
    except:
        player1.difficulty = Difficulty(0)  # unlock_all_cheat 

    sounds.difficulty_select_sound()
    _difficulty_set_health()


def go_to_checkpoint():  # main program running movement to levels -- checkpoint when leaving area
    checkpoints = {'1': outside_area,
                   '2': diner_area,
                   '3': gas_station,
                   '4': parkview_area,
                   '5': broken_roads_area,
                   '6': ch1_good_ending,
                   '7': ch1_bad_ending,
                   }
    while 'exit' not in player1.check_point:
        if 'bad' in player1.check_point:
            checkpoints['7']()
        else:
            checkpoints[player1.check_point]()


# move to player class
def print_health(player_difficulty, message, sleep_duration=0):
    if player_difficulty == Difficulty(1):
        print_green(message, sleep_duration)
    elif player_difficulty == Difficulty(2):
        print_yellow(message, sleep_duration)
    elif player_difficulty == Difficulty(3):
        print_red(message, sleep_duration)

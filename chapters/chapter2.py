from sys import exit
from time import sleep
# from classes import Player, Difficulty
from other.sounds_effects import GameSounds
from game import player1, sounds, Difficulty
from choices import _player_choice, error_message
from other.colors import print_green, print_yellow, print_red, print_s


def start():
    print_green('Welcome to Chapter 2!\n', 1)
    continue_message()


def ch2_good_ending():
    """When the player has successfully reached the end of the game."""
    sounds.good_luck()
    print_green('Congratulations, you have survived Chapter 2..\n', 1)
    print_green(f'You survived with a total of {player1.health} health left!\n', 1)

    difficulty_achievement = {Difficulty(1): ('2', 'Common'),
                              Difficulty(2): ('2', 'Uncommon'),
                              Difficulty(3): ('2', 'Rare'),
                              Difficulty(0): ('1', 'Cheater'),
                              }
    print_green(player1.print_achievement(difficulty_achievement[player1.difficulty]), 2)
    # check if all other achievements are unlocked
    all_achievements = player1.print_achievement(('1', 'Ultra Rare'))
    if all_achievements:
        print_green(all_achievements)
    sounds.good_luck()
    restart()


def ch2_bad_ending():
    """When the player dies at any point."""
    sounds.ch1_bad_ending()
    print_red('You have died and not reached the end of the horrors...\n', 1)
    restart()


def restart():
    """Allows the players to restart their game and reset their saved data values"""
    from gameprocess import game_intro, game, go_to_checkpoint
    choices = ['y', 'yes', 'n', 'no']
    choice_options = ['Would you like to restart the game (yes / no): ']
    restart_choice = _player_choice(choices, choice_options)

    if restart_choice in ['y', 'yes']:
        player1.reset_values(0, 100, False)
        sounds.set_volume(0.05)
        print_green('Default stats have been loaded/saved and a new game will begin...\n', 1)
        player1.check_point = player1.check_point.replace('bad', '')  # load game from last checkpoint
        game_intro()
        game()
        go_to_checkpoint()
    elif restart_choice in ['n', 'no']:
        print_s('Ending game...', 1)
        exit()


def continue_message():
    """Only for development purposes and has no impact on the game"""
    print_s('Continue here...', 3)
    exit(1)

""" This file holds all the chapter 2 areas of the game. """
from sys import exit
from time import sleep
# from classes import Player, Difficulty
from other.sounds_effects import GameSounds
from game import player1, sounds, Difficulty
from choices import _player_choice, error_message
from other.colors import print_green, print_yellow, print_red, print_sleep


def start():
    """start of ch2"""
    sounds.intro_sounds()
    print_green('Welcome to Chapter 2!\n', 3)
    print_sleep('Upon driving the car through the broken roads area, the sun is certainly dwindling and time in the car'
                'says 2:35 AM.\nYou continue to grow yourself tired and restless from everything that had led to this '
                'point\n', 2.5)
    choices = [str(x) for x in range(1, 3)]
    choice_options = [
        'Due to the car getting low on gas, you must make a tough decision. (1) Drive back to the local gas station in '
        'town (2) Turn off the car and set up a camp fire in the woods: ']
    choice = _player_choice(choices, choice_options)

    if choice == '1':
        sounds.zombie_attack_inside()
        print_sleep('While attempting to put the car in reverse and head backwards to the local gas station in town, '
                    'a swarm of zombies arise on the car while the car gets stuck into gear!\n', 2.5)
        if not player1.user_attack():
            return
        player1.total_kills += 5
        print_green('You have successfully killed off the heaping swarm of zombies surrounding the car!\n', 1)
        continue_message()
    elif choice == '2':
        print_sleep(
            'You have parked the car near the closet woods area and now need to gather up some supplies for a camp '
            'fire.\n', 1)
        continue_message()


def ch2_good_ending():
    """When the player has successfully reached the end of the game."""
    sounds.good_luck()
    print_green('Congratulations, you have survived Chapter 2...\n', 1)
    print_green(f'You survived with a total of {player1.health} health left!\n', 1)

    difficulty_achievement = {Difficulty(1): ('2', 'Common'),
                              Difficulty(2): ('2', 'Uncommon'),
                              Difficulty(3): ('2', 'Rare'),
                              Difficulty(0): ('1', 'Cheater'),
                              }
    player1.print_achievement(difficulty_achievement[player1.difficulty])
    # check if all other achievements are unlocked
    all_achievements = player1.print_achievement(('1', 'Ultra Rare'))
    if all_achievements:
        print_green(all_achievements)
    sounds.good_luck()
    restart()


def ch2_bad_ending():
    """When the player dies at any point."""
    sounds.bad_ending()
    print_red('You have died and not reached the end of the horrors...\n', 1)
    restart()


def restart():
    """Allows the players to restart their game and reset their saved data values"""
    from gameprocess import difficulty, game, go_to_checkpoint
    choices = ['y', 'yes', 'n', 'no']
    choice_options = ['Would you like to restart the game (yes / no): ']
    restart_choice = _player_choice(choices, choice_options)

    if restart_choice in ['y', 'yes']:
        player1.reset_values(0, 100, False)
        sounds.set_volume(0.05)
        print_green('Default stats have been loaded/saved and a new game will begin...\n', 1)
        player1.check_point = player1.check_point.replace('bad', '')  # load game from last checkpoint
        difficulty()
        game()
        go_to_checkpoint()
    elif restart_choice in ['n', 'no']:
        print_sleep('Ending game...', 1)
        exit()


def continue_message():
    """Only for development purposes and has no impact on the game"""
    print_sleep('Continue here...', 3)
    exit(1)

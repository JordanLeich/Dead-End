""" This file holds all the chapter 3 areas of the game. """
import sys
from time import sleep
from other.sounds_effects import GameSounds
from game import player1, sounds, Difficulty
from choices import _player_choice, error_message
from other.colors import print_green, print_yellow, print_red, print_sleep, print_blue


class Chapter:
    """Contains many of the essential functions used to traverse through the main game."""
    def start(self):
        """start of chapter"""
        sounds.intro_sounds()
        print_green(f'Welcome to Chapter {self.chapter_num}!\n', 3)
        player1.chapter = self.chapter_num

    def good_ending(self):
        """When the player has successfully reached the end of the game."""
        sounds.good_luck()
        print_green(f'Congratulations, you have survived Chapter {self.chapter_num}...\n', 1)
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

    def bad_ending(self):
        """When the player dies at any point."""
        sounds.bad_ending()
        print_red('You have died and not reached the end of the horrors...\n', 1)
        self.restart()

    def restart(self):
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
            sys.exit()

    def continue_message(self):
        """Only for development purposes and has no impact on the game"""
        print_sleep('Continue here...', 3)
        sys.exit()

""" This file holds all the chapter 2 areas of the game. """
from time import sleep
# from classes import Player, Difficulty
from chapters.chapter import Chapter
from chapters.chapter3 import Chapter3

from other.sounds_effects import GameSounds
from game import player1, sounds, Difficulty
from choices import _player_choice, error_message
from other.colors import print_green, print_yellow, print_red, print_sleep, print_blue

chapter3 = Chapter3()


class Chapter2(Chapter):
    """Contains all the main chapter 2 areas of the game."""
    chapter_num = 2

    def checkpoints(self):
        """runs movement to levels -- checkpoint when leaving area"""
        return {'0': self.game,
                '1': self.good_ending_and_continue,
                '2': self.bad_ending,
                }

    def good_ending_and_continue(self):
        """Simply plays the good ending scene and then drops the player into chapter 2."""
        self.good_ending()
        Chapter3().game()

    def game(self):
        """start of ch2"""
        self.start()
        print_sleep(
            'Upon driving the car through the broken roads area, the sun is certainly dwindling and time in the car'
            'says 2:35 AM.\nYou continue to grow yourself tired and restless from everything that had led to this '
            'point\n', 2.5)
        choices = [str(x) for x in range(1, 3)]
        choice_options = [
            'Due to the car getting low on gas, you must make a tough decision. (1) Drive back to the local gas '
            'station in town (2) Turn off the car and set up a camp fire in the woods: ']
        choice = _player_choice(choices, choice_options)

        if choice == '1':
            sounds.zombie_attack_inside()
            print_sleep(
                'While attempting to put the car in reverse and head backwards to the local gas station in town, '
                'a swarm of zombies arise on the car while the car gets stuck into gear!\n', 2.5)
            if not player1.user_attack():
                return
            player1.total_kills += 5
            print_green('You have successfully killed off the heaping swarm of zombies surrounding the car!\n', 1)
            self.continue_message()
        elif choice == '2':
            print_sleep(
                'You have parked the car near the closet woods area and now need to gather up some supplies for a camp '
                'fire.\n', 1)
            self.continue_message()

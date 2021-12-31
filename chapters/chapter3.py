""" This file holds all the chapter 3 areas of the game. """
# from classes import Player, Difficulty
from chapters.chapter import Chapter
#from chapters.chapter4 import Chapter4

from other.sounds_effects import GameSounds
from game import player1, sounds, Difficulty
from choices import _player_choice, error_message
from other.colors import print_green, print_yellow, print_red, print_sleep, print_blue


class Chapter3(Chapter):
    chapter_num = 3

    def checkpoints(self):
        """runs movement to levels -- checkpoint when leaving area"""
        return {'0': self.game,
                '1': self.good_ending_and_continue,
                '2': self.bad_ending,
                }

    def good_ending_and_continue(self):
        self.good_ending()
        #Chapter4.game()


    def game(self):
        """start of ch2"""
        self.start()
        self.continue_message()

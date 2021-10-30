from random import randint
from enum import Enum
from copy import deepcopy


class Player:
    """
This class is to setup the player with all variables needed through out the game.
If more variables are needed. they can be added here.
    """

    def __init__(self, balance=0, health=0, difficulty=2, knife=False, ak47=False, pistol=False, bat=False,
                 rpg=False, barrett=False, spell=False):
        # user attributes
        self.balance = balance
        self.health = health
        self.difficulty = Difficulty(difficulty)
        # user weapons
        self.weapon_dict = {
        #Data organized: '#': ['name', 'cost', 'purchased', 'health_rand_1', 'health_rand_2'],
            '0': ['knife', None, knife, 40, 45], # found weapon
            '1': ['Spiked Baseball Bat', 5, bat, 30, 40],
            '2': ['1997 Beretta Pistol', 15, pistol, 20, 30],
            '3': ['1999 AK-47 Assault Rifle', 25, ak47, 10, 20],
            '4': ['1999 Semi-automatic Barrett Sniper Rifle', 60, barrett, 3, 10],
            '5': ['Rocket Missile Launcher', 100, rpg, 0, 0],
            '6': ['The Merchants Strange Spell', 125, spell, -30, -10],
        }
        #  check point location
        self.check_point = ''

    def get_data(self):
        value_dict = vars(self)
        value_dict['difficulty'] = self.difficulty
        return value_dict

    def load_data(self, user_data):
        """This function will set player data from previous game"""
        self.balance = user_data['balance']
        self.health = user_data['health']
        # self.merchant_luck = user_data['merchant_luck']
        self.difficulty = Difficulty(int(user_data['difficulty']))
        # self.weapon_dict = user_data['weapon_dict']
        self.check_point = user_data['check_point']

    def get_money(self, start_int=5, end_int=30):
        random_money = randint(start_int, end_int)
        self.balance += random_money
        return random_money

    def lose_health(self, start_int, end_int):
        random_health = randint(start_int, end_int)
        self.health -= random_health
        return random_health

    def get_health(self, start_int, end_int):
        random_health = randint(start_int, end_int)
        self.health += random_health
        return random_health

    def use_item(self, key):
        return self.lose_health(self.weapon_dict[key][-2], self.weapon_dict[key][-1])


# Difficulty labeling - easier for referencing + printing
class Difficulty(Enum):
    God = 0
    Easy = 1
    Medium = 2
    Hard = 3

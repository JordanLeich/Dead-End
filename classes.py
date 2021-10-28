from random import randint
from enum import Enum
from copy import deepcopy


class Player:
    """
This class is to setup the player with all variables needed through out the game.
If more variables are needed. they can be added here.
    """

    def __init__(self, balance=0, health=0, luck=0, difficulty=2, knife=False, ak47=False, pistol=False, bat=False,
                 rpg=False, barrett=False, spell=False, continue_buying=False):
        # user attributes
        self.balance = balance
        self.health = health
        self.merchant_luck = luck
        self.difficulty = Difficulty(difficulty)
        self.continue_buying = continue_buying
        # user weapons
        self.starting_knife = knife
        self.ak_47_rifle = ak47
        self.barrett_rifle = barrett
        self.beretta_pistol = pistol
        self.baseball_bat = bat
        self.rocket_launcher = rpg
        self.spell = spell
        #  check point location
        self.check_point = ''

    def get_data(self):
        value_dict = deepcopy(vars(self))
        value_dict['difficulty'] = self.difficulty.value
        return value_dict

    def load_data(self, user_data):
        """This function will set player data from previous game"""
        self.balance = user_data['balance']
        self.health = user_data['health']
        self.merchant_luck = user_data['merchant_luck']
        self.difficulty = Difficulty(int(user_data['difficulty']))
        self.starting_knife = user_data['starting_knife']
        self.baseball_bat = user_data['baseball_bat']
        self.beretta_pistol = user_data['beretta_pistol']
        self.ak_47_rifle = user_data['ak_47_rifle']
        self.barrett_rifle = user_data['barrett_rifle']
        self.rocket_launcher = user_data['rocket_launcher']
        self.spell = user_data['spell']
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


# Difficulty labeling - easier for referencing + printing
class Difficulty(Enum):
    God = 0
    Easy = 1
    Medium = 2
    Hard = 3

from random import randint
from enum import Enum
from copy import deepcopy


class Player:
    """
This class is to setup the player with all variables needed through out the game.
If more variables are needed. they can be added here.
    """

    def __init__(self, balance=0, health=0, difficulty=-1):
        # user attributes
        self.balance = balance
        self.health = health
        self.difficulty = Difficulty(difficulty)
        self.weapon_dict = {
            # Organized: '#': ['name', 'cost', 'purchased', 'health_rand_1', 'health_rand_2'],
            '0': ['Knife', None, False, 40, 45],  # Weapon can be found in-game at the start
            '1': ['Spiked Baseball Bat', 5, False, 30, 40],
            '2': ['1997 Beretta Pistol', 15, False, 20, 30],
            '3': ['1999 AK-47 Assault Rifle', 25, False, 10, 20],
            '4': ['1999 Semi-automatic Barrett Sniper Rifle', 60, False, 3, 10],
            '5': ['Rocket Missile Launcher', 100, False, 0, 0],
            '6': ['The Merchants Strange Spell', 125, False, -30, -10],
        }
        self.consumables = [  # only usable during purchase
            # Organized: ['name', 'cost', 'purchased', 'health_rand_1', 'health_rand_2'],
            ['Apple', 10, False, 5, 15],
            ['Body Armor', 50, False, 40, 60],
        ]
        self.check_point = ''
        self.achievement_list = {
            ('1', 'Common'): {'name': 'Slice & Dice',
                              'desc': 'Find a hidden knife.', 
                              'unlocked': False,
                              },
            ('2', 'Common'): {'name': 'Survivor',
                              'desc': 'Beat the game on Easy Mode.',
                              'unlocked': False,
                              },
            ('1', 'Uncommon'): {'name': 'Family Memories',
                                'desc': 'You found a family picture of a man you met prior.', 
                                'unlocked': False,
                                },
            ('2', 'Uncommon'): {'name': 'Battle Hardened',
                                'desc': 'Beat the game on Medium Mode.', 
                                'unlocked': False,
                                },
            ('1', 'Rare'): {'name': 'Unstoppable Juggernaut',
                            'desc': 'You have obtained a total of 500 Health or more.', 
                            'unlocked': False,
                            },
            ('2', 'Rare'): {'name': 'Ruthless Maniac',
                            'desc': 'Beat the game on Hard Mode.', 
                            'unlocked': False,
                            },
            ('3', 'Rare'): {'name': 'Wicked Happenings',
                            'desc': 'You purchased the merchants secret spell.', 
                            'unlocked': False,
                            },
            ('1', 'Ultra Rare'): {'name': 'Perfection Indeed',
                                  'desc': 'Obtain all achievements.', 
                                  'unlocked': False,
                                  },
        }


    def get_data(self) -> dict:
        value_dict = deepcopy(vars(self))
        value_dict['difficulty'] = self.difficulty.value
        return value_dict

    def load_data(self, user_data=None) -> None:
        """This function will set player data from previous game"""
        if user_data is None:
            return
        self.balance = user_data['balance']
        self.health = user_data['health']
        self.difficulty = Difficulty(int(user_data['difficulty']))
        self.weapon_dict = user_data['weapon_dict']
        self.consumables = user_data['consumables']
        self.check_point = user_data['check_point']

    def get_money(self, start_int=5, end_int=30) -> int:
        random_money = randint(start_int, end_int)
        self.balance += random_money
        return random_money

    def lose_health(self, start_int, end_int) -> int:
        random_health = randint(start_int, end_int)
        self.health -= random_health
        return random_health

    def get_health(self, start_int, end_int) -> int:
        random_health = randint(start_int, end_int)
        self.health += random_health
        return random_health

    def use_item(self, key) -> int:
        return self.lose_health(self.weapon_dict[key][-2], self.weapon_dict[key][-1])

    def consume(self, index) -> int:
        return self.get_health(self.consumables[index][-2], self.consumables[index][-1])

    def set_difficulty(self, difficulty) -> None:
        self.difficulty = Difficulty(difficulty)

    def reset_values(self, balance, health, default_value) -> None:
        self.balance = balance
        self.health = health
        for k, v in self.weapon_dict.items():
                v[2] = default_value
        for v in self.consumables:
            v[2] = default_value

    def print_achievement(self, achievement: tuple) -> str:
        item = self.achievement_list(achievement)
        if item['unlocked']: # achievement already unlocked
            return
        item['unlocked'] = True
        return f'{achievement[1]} Achievement Unlocked! {item["name"]} - {item["des"]}\n'


# Difficulty labeling - easier for referencing + printing
class Difficulty(Enum):
    Notset = -1
    God = 0
    Easy = 1
    Medium = 2
    Hard = 3

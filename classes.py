""" Holds the player class along with important functions that control the achievements, xp system, and much more. """
from random import randint
from enum import Enum
from copy import deepcopy
from other.colors import print_green, print_yellow, print_red, print_sleep, print_blue
from gamedata import GameData
from choices import _player_choice

game_data = GameData()  # load/save functions Instance


class Player:
    """This class is to set up the player with all variables needed throughout the game. If more variables are
    needed. they can be added here. """

    def __init__(self, balance=0, health=0, difficulty=-1, xp_amount=0, user_level=0, player_deaths=0, total_kills=0,
                 start_timer=0):
        # user attributes
        self.balance = balance
        self.health = health
        self.difficulty = Difficulty(difficulty)
        self.xp_amount = xp_amount
        self.user_level = user_level
        self.player_deaths = player_deaths
        self.total_kills = total_kills
        self.start_timer = start_timer
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
        self.chapter = 0
        self.check_point = ''
        self.achievement_list = {
            ('1', 'Common'): {'name': 'Slice & Dice',
                              'desc': 'Find a hidden knife.',
                              'unlocked': False,
                              },
            ('2', 'Common'): {'name': 'Survivor',
                              'desc': 'Beat a chapter on Easy Mode.',
                              'unlocked': False,
                              },
            ('3', 'Common'): {'name': 'Welcome to the Pit',
                              'desc': 'Experience death for the first time.',
                              'unlocked': False,
                              },
            ('1', 'Uncommon'): {'name': 'Family Memories',
                                'desc': 'You found a family picture of a man you met prior.',
                                'unlocked': False,
                                },
            ('2', 'Uncommon'): {'name': 'Battle Hardened',
                                'desc': 'Beat a chapter on Medium Mode.',
                                'unlocked': False,
                                },
            ('3', 'Uncommon'): {'name': 'The Grim Reaper',
                                'desc': 'Die a total of 5 times.',
                                'unlocked': False,
                                },
            ('4', 'Uncommon'): {'name': 'Getting the hang of it',
                                'desc': 'Obtain a total of 5 kills.',
                                'unlocked': False,
                                },
            ('1', 'Rare'): {'name': 'Unstoppable Juggernaut',
                            'desc': 'You have obtained a total of 500 Health or more.',
                            'unlocked': False,
                            },
            ('2', 'Rare'): {'name': 'Ruthless Maniac',
                            'desc': 'Beat a chapter on Hard Mode.',
                            'unlocked': False,
                            },
            ('3', 'Rare'): {'name': 'Wicked Happenings',
                            'desc': 'You purchased the merchants secret spell.',
                            'unlocked': False,
                            },
            ('4', 'Rare'): {'name': 'Maximum Potential',
                            'desc': 'Reached the maximum in-game XP level.',
                            'unlocked': False,
                            },
            ('5', 'Rare'): {'name': 'Rags to Riches',
                            'desc': 'Obtained a total of 250 dollars or more.',
                            'unlocked': False,
                            },
            ('6', 'Rare'): {'name': 'Dark Souls Inspired',
                            'desc': 'Die a total of 10 times.',
                            'unlocked': False,
                            },
            ('7', 'Rare'): {'name': 'Merciful Slayer',
                            'desc': 'Obtain a total of 25 kills.',
                            'unlocked': False,
                            },
            ('1', 'Ultra Rare'): {'name': 'Perfection Indeed',
                                  'desc': 'Obtain all achievements.',
                                  'unlocked': False,
                                  },
            ('2', 'Ultra Rare'): {'name': 'Fifthly Rich',
                                  'desc': 'Obtain a total of 1000 dollars or more.',
                                  'unlocked': False,
                                  },
            ('3', 'Ultra Rare'): {'name': 'Relentless Rampage',
                                  'desc': 'Obtain a total of 50 kills.',
                                  'unlocked': False,
                                  },
            ('1', 'Cheater'): {'name': 'Cheater',
                               'desc': 'Complete a chapter the wrong way',
                               'unlocked': False,
                               }
        }
        self.xp_amount = 0
        self.user_level = 0

    def get_data(self) -> dict:
        """used to get data from achievements and difficulty"""
        value_dict = deepcopy(vars(self))
        value_dict['difficulty'] = self.difficulty.value
        value_dict['achievement_list'] = {}
        for k, v in self.achievement_list.items():
            value_dict['achievement_list'][' '.join(k)] = v
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
        for k, v in user_data['achievement_list'].items():
            self.achievement_list[(k.split(' ', 1)[0], k.split(' ', 1)[1])] = v
        self.xp_amount = user_data['xp_amount']
        self.user_level = user_data['user_level']
        self.player_deaths = user_data['player_deaths']
        self.total_kills = user_data['total_kills']

    def get_money(self, start_int=5, end_int=30) -> int:
        """sends money to the players balance"""
        random_money = randint(start_int, end_int)
        self.balance += random_money
        return random_money

    def lose_health(self, start_int, end_int) -> int:
        """subtracts health from the players health"""
        random_health = randint(start_int, end_int)
        self.health -= random_health
        return random_health

    def get_health(self, start_int, end_int) -> int:
        """adds health to the players health"""
        random_health = randint(start_int, end_int)
        self.health += random_health
        return random_health

    def use_item(self, key) -> int:
        """allows the player to use a weapon of their choice while still losing health in an attack"""
        return self.lose_health(self.weapon_dict[key][-2], self.weapon_dict[key][-1])

    def consume(self, index) -> int:
        """allows the player to gain health via consumables"""
        return self.get_health(self.consumables[index][-2], self.consumables[index][-1])

    def set_difficulty(self, difficulty) -> None:
        """sets the class difficulty to the function variable named difficulty"""
        self.difficulty = Difficulty(difficulty)

    def reset_values(self, balance, health, default_value) -> None:
        """resets the player's health, balance, owned items to a set amount"""
        self.balance = balance
        self.health = health
        for k, v in self.weapon_dict.items():
            v[2] = default_value
        for v in self.consumables:
            v[2] = default_value

    def print_achievement(self, achievement: tuple) -> None:
        """prints an achievement that gets unlocked"""
        item = self.achievement_list[achievement]
        if item['unlocked']:  # achievement already unlocked
            return
        # specific achievement checks
        if achievement == ('1', 'Ultra Rare'):  # all other achievements unlocked
            item = all(v['unlocked'] for k, v in self.achievement_list.items()
                       if k != achievement)

            if not item:  # not all achievements are unlocked
                return

        item['unlocked'] = True
        message = f'{achievement[1]} Achievement Unlocked! {item["name"]} - {item["desc"]}\n'
        from game import sounds
        sounds.good_luck()
        print_blue(message, 2)

    def merchant(self):  # sourcery no-metrics
        """Merchant randomly shows up, allowing the player to purchase weapons and consumables"""
        from game import sounds
        if self.health <= 0:  # end game if no health
            print_red('You currently have no health left...\n', 1)
            self.check_point = f'{self.check_point}bad'

        if randint(1, 7) != 3:  # Random chance for player to interact with merchant
            return
        sounds.good_luck()
        print_green('Whoosh! The lucky merchant has appeared in-front of you...\n', 1)
        if self.balance <= 0:
            print_yellow('Uh-Oh! You do not have enough money to buy anything... keep playing to acquire more money!\n',
                         1)
            return

        choices = ['b', 'buy', 'y', 'yes', 's', 'skip', 'n', 'no']
        choice_options = ['Would you like to buy from the merchant or skip past the merchant (buy / skip): ']
        choice = _player_choice(choices, choice_options)

        if choice in ['b', 'buy', 'y', 'yes']:
            buy_item = ''
            num_item = len(self.weapon_dict)
            total_items = num_item + len(self.consumables)
            exit_merchant_menu = str(total_items)

            weapon_choices = [f"({k}) {v[0]} ({v[1]} Dollars)" for k, v in self.weapon_dict.items() if
                              k != '0' and not v[2]]
            consumables = [f"({c + num_item}) {v[0]} ({v[1]} Dollars)" for c, v in enumerate(self.consumables)]
            choice_options = ['--- Merchants inventory ---']
            choice_options.extend(weapon_choices)
            choice_options.extend(consumables)
            choice_options.extend([f'({exit_merchant_menu}) Exit The Merchant Shop\n',
                                   'What would you like to buy: ',
                                   ])
            while buy_item != exit_merchant_menu:
                print_green(f'Health: {self.health}\n', 1)
                print_green(f'Balance: {self.balance}\n', 1)
                buy_item = _player_choice([str(x) for x in range(1, total_items + 1)], choice_options)
                consumable_index = int(buy_item) - num_item

                if buy_item == exit_merchant_menu:
                    print_sleep('The merchant bids you a farewell and good luck!\n', 1)
                    break
                elif consumable_index >= 0 and self.balance > self.consumables[consumable_index][1]:
                    self.balance -= self.consumables[consumable_index][1]
                    print_green(
                        f'You have used the {self.consumables[consumable_index][0]}, giving you a bonus '
                        f'of {self.consume(consumable_index)} health.\n', 2)
                elif self.balance >= self.weapon_dict[buy_item][1]:
                    sounds.merchant_purchase_sound()
                    self.balance -= self.weapon_dict[buy_item][1]
                    self.weapon_dict[buy_item][2] = True
                    print_green(f'{self.weapon_dict[buy_item][0]} has been purchased!\n', 1)
                    if buy_item == '6':
                        self.print_achievement(('3', 'Rare'))
                        print_green('As the Merchant hands you his own crafted spell, he tells you that you now '
                                    'wield true pain to foes whilst providing restoration to thine self.\n', 2.5)
                else:
                    print_yellow('Sorry, not enough available funds to purchase that item!\n', 2)
        elif choice in ['s', 'skip', 'n', 'no']:
            print_sleep('The merchant has been skipped but can be brought back later...\n', 1)

    def user_attack(self, enemy='zombies'):
        """used whenever the player gets in a battle with a zombie"""
        choice_names = [v[0] for k, v in self.weapon_dict.items() if v[2]]
        if not choice_names:  # no choice for them to make
            self.health = 0
            print_red('Due to not having any available weapons on you... You try to defend yourself...\nThe zombie '
                      'overpowers you! Game Over!\n', 3)
            self.check_point = f'{self.check_point}bad'
            return False

        print('--- All owned items ---\n')
        choices = [str(c + 1) for c, _ in enumerate(choice_names)]
        choice_options = [f'({c + 1}) {v}' for c, v in enumerate(choice_names)]
        choice_options.extend(['\nWhich item would you like to use: '])
        choice = _player_choice(choices, choice_options)

        key = str(deep_index(list(self.weapon_dict.values()), choice_names[int(choice) - 1]))

        if key == '6':
            print_green(
                f'You have used the Merchants Strange Spell and defeated the {enemy} without losing any health! '
                f'\nThrough the power of the Strange Spell, you gain {self.get_health(10, 30)} health through its '
                f'restoration casting!\n', 3.5)
        else:  # print color based on user health
            lost_health = self.use_item(key)
            if lost_health > self.health:
                print_red(f'The {enemy} overpowered you. Losing all of your health...\n', 1)
                self.check_point = f'{self.check_point}bad'
                return False
            message = f'You have used the {self.weapon_dict[key][0]} and defeated the {enemy} losing {lost_health}' \
                      f' health!\n '
            if self.health < 25:
                print_red(message, 2)
            elif self.health < 50:
                print_yellow(message, 2)
            else:
                print_green(message, 2)
            from gameprocess import xp_level_system
            xp_level_system()
        return True  # attack successful

    def checkpoint_save(self, checkpoint_name=''):
        """activates a checkpoint save and writes to the data.json file, also allows the user to continue playing or
        not """
        self.check_point = checkpoint_name
        game_data.save_game(self.get_data())  # Sends self info to save file
        if self.health <= 0:  # extra check to see if the player has no more health left.
            print_red('Sorry you have no more health! You have lost the game!\n', 1)
            return  # restart()
        elif self.total_kills == 5:
            self.print_achievement(('4', 'Uncommon'))
        elif self.total_kills == 25:
            self.print_achievement(('7', 'Rare'))
        elif self.total_kills == 50:
            self.print_achievement(('3', 'Ultra Rare'))
        if checkpoint_name != '':  # remove checkpoint printing for ending + difficulty selected
            self.merchant()
            print_green('A checkpoint has been reached, Your in-game stats will now be displayed.\n', 1)
            print_green(f'Health: {self.health}')
            print_green(f'Balance: {self.balance}')
            print_green(f'XP Amount: {self.xp_amount}')
            print_green(f'XP Level: {self.user_level}\n', 1)
            choices = ['y', 'yes', 'n', 'no']
            choice_options = ['Would you like to continue the game (yes / no): ']
            exit_choice = _player_choice(choices, choice_options)
            if exit_choice in ['n', 'no']:  # ask player if they would like to quit ~ returns to menu
                self.check_point = f'{checkpoint_name}exit'


def deep_index(lst, w):
    """helper function for user_attack to find the corresponding item in weapon_dict"""
    return [i for (i, sub) in enumerate(lst) if w in sub][0]


class Difficulty(Enum):
    """Difficulty labeling - easier for referencing + printing"""
    Notset = -1
    God = 0
    Easy = 1
    Medium = 2
    Hard = 3

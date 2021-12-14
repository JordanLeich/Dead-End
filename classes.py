from random import randint
from enum import Enum
from copy import deepcopy
# new imports to fix
from other.colors import print_green, print_yellow, print_red, print_s
from gamedata import GameData
from choices import _player_choice, error_message

game_data = GameData()  # load/save functions Instance


class Player:
    """
This class is to setup the player with all variables needed through out the game.
If more variables are needed. they can be added here.
    """
    def __init__(self, balance=0, health=0, difficulty=-1, xp_amount=0, user_level=0):
        # user attributes
        self.balance = balance
        self.health = health
        self.difficulty = Difficulty(difficulty)
        self.xp_amount = xp_amount
        self.user_level = user_level
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
            ('1', 'Cheater'): {'name': 'Cheater',
                               'desc': 'Complete a chapter the wrong way',
                               'unlocked': False,
                               }
        }

    def get_data(self) -> dict:
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
        item = self.achievement_list[achievement]
        if item['unlocked']:  # achievement already unlocked
            return
        # specific achievement checks
        if achievement == ('1', 'Ultra Rare'):  # all other achievements unlocked
            item = all(
                [v['unlocked']
                for k, v in self.achievement_list.items()
                if k != achievement]
            )

            if not item:  # not all achievements are unlocked
                return

        item['unlocked'] = True
        return f'{achievement[1]} Achievement Unlocked! {item["name"]} - {item["desc"]}\n'

    def merchant(self):
        """
    Merchant randomly shows up, allowing the player to purchase weapons and consumables.
        """
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
                    print_s('The merchant bids you a farewell and good luck!\n', 1)
                    break
                elif consumable_index >= 0 and self.balance > self.consumables[consumable_index][1]:
                    self.balance -= self.consumables[consumable_index][1]
                    print_green(
                        f'You have used the {self.consumables[consumable_index][0]}, giving you a bonus of {self.consume(consumable_index)} health.\n',
                        2)
                elif self.balance >= self.weapon_dict[buy_item][1]:
                    sounds.merchant_purchase_sound()
                    self.balance -= self.weapon_dict[buy_item][1]
                    self.weapon_dict[buy_item][2] = True
                    print_green(f'{self.weapon_dict[buy_item][0]} has been purchased!\n', 1)
                    if buy_item == '6':
                        print_green(self.print_achievement(('3', 'Rare')), 2)
                        print_green(
                            'As the Merchant hands you his own crafted spell, he tells you that you now wield true pain to foes whilst providing restoration to thine self.\n',
                            2.5)
                else:
                    print_yellow('Sorry, not enough available funds to purchase that item!\n', 2)
        elif choice in ['s', 'skip', 'n', 'no']:
            print_s('The merchant has been skipped but can be brought back later...\n', 1)

    def user_attack(self, enemy='zombies'):
        from game import sounds

        """For fights with zombies or humans. User choice of weapon to use"""
        choice_names = [v[0] for k, v in self.weapon_dict.items() if v[2]]
        if not choice_names:  # no choice for them to make
            self.health = 0
            print_red(
                'Due to not having any available weapons on you... You try to defend yourself...\nThe zombie overpowers you! Game Over!\n',
                3)
            self.check_point = f'{self.check_point}bad'
            return False

        choices = [str(c + 1) for c, _ in enumerate(choice_names)]
        choice_options = [f'({c + 1}) {v}' for c, v in enumerate(choice_names)]
        choice_options.extend(['\nWhich item would you like to use: '])
        choice = _player_choice(choices, choice_options)

        key = str(deep_index(list(self.weapon_dict.values()), choice_names[int(choice) - 1]))

        if key == '6':
            print_green(
                f'You have used the Merchants Strange Spell and defeated the {enemy} without losing any health! \nThrough the power of the Strange Spell, you gain {self.get_health(10, 30)} health through its restoration casting!\n',
                3.5)
        else:  # print color based on user health
            lost_health = self.use_item(key)
            if lost_health > self.health:
                print_red(f'The {enemy} overpowered you. Losing all of your health...\n', 1)
                self.check_point = f'{self.check_point}bad'
                return False
            message = f'You have used the {self.weapon_dict[key][0]} and defeated the {enemy} losing {lost_health} health!\n'
            if self.health < 25:
                print_red(message, 2)
            elif self.health < 50:
                print_yellow(message, 2)
            else:
                print_green(message, 2)
        return True  # attack successful

    def checkpoint_save(self, checkpoint_name=''):
        self.check_point = checkpoint_name
        game_data.save_game(self.get_data())  # Sends self info to save file
        if self.health <= 0:  # shouldn't really get to this point --> TODO
            print_red('Sorry you have no more health! You have lost the game!\n', 1)
            return  # restart()
        if checkpoint_name != '':  # remove checkpoint printing for ending + difficulty selected
            self.merchant()
            print_green('A checkpoint has been reached...\n', .5)
            print_green(f'Health: {self.health}\n', 1)
            print_green(f'Balance: {self.balance}\n', 1)

            choices = ['y', 'yes', 'n', 'no']
            choice_options = ['Would you like to continue the game (yes / no): ']
            exit_choice = _player_choice(choices, choice_options)
            if exit_choice in ['n', 'no']:  # ask player if they would like to quit ~ returns to menu
                self.check_point = f'{checkpoint_name}exit'

    def xp_level_system(self, xp_amount=0, user_level=0):
        self.xp_amount = xp_amount
        self.user_level = user_level

        if xp_amount >= 400 and xp_amount <= 499:
            user_level = 4
            print_green('Current XP Level - 4\n', 1)
        elif xp_amount >= 300 and xp_amount <= 399:
            user_level = 3
            print_green('Current XP Level - 3\n', 1)
        elif xp_amount >= 200 and xp_amount <= 299:
            user_level = 2
            print_green('Current XP Level - 2\n', 1)
        elif xp_amount <= 199:
            user_level = 1
            print_green('Current XP Level - 1\n', 1)
        else:
            print_green('Reached Maximum XP Level - 5\n', 1)
            user_level = 5

    def award_xp_to_player(self):
        if Difficulty == 1:
            self.xp_amount += randint(15, 75)
        elif Difficulty == 2:
            self.xp_amount += randint(30, 75)
        elif Difficulty == 3:
            self.xp_amount += randint(75, 100)
        else:
            self.xp_amount += randint(1, 100)


# helper function for user_attack to find the corresponding item in weapon_dict
def deep_index(lst, w):
    return [i for (i, sub) in enumerate(lst) if w in sub][0]


# Difficulty labeling - easier for referencing + printing
class Difficulty(Enum):
    Notset = -1
    God = 0
    Easy = 1
    Medium = 2
    Hard = 3

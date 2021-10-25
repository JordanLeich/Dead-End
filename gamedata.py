import json
from os.path import exists as file_exists
from other import colors

class Game_data:
    """This class will offer loading and saving of game data for
    Zombie-Survival-Game."""

    def __init__(self):
        self.file = 'data.json'
        self.file_exists = True if file_exists(self.file) else False

    def load_game(self, player1: object):
        if self.file_exists:
            with open(self.file, 'r') as user_data_file:
                user_data = json.load(user_data_file)
                player1.user_balance = user_data['Balance']
                player1.user_health = user_data['Health']
                player1.merchant_luck = user_data['Merchant Luck']
                player1.user_difficulty = user_data['Difficulty']
                player1.starting_knife = user_data['Starting Knife']
                player1.baseball_bat = user_data['Baseball Bat']
                player1.beretta_pistol = user_data['Beretta Pistol']
                player1.ak_47_rifle = user_data['AK 47 Rifle']
                player1.rocker_launcher = user_data['Rocket Missile Launcher']
                print(colors.green + 'Saved data has been loaded successfully!\n', colors.reset)
                user_data_file.close()
        else:
            print(colors.yellow + 'No saved data found...\n\n' + colors.reset,
                  colors.green + 'Starting a fresh game...\n' + colors.reset)
            player1.user_balance = 0
            player1.user_health = 0
            player1.merchant_luck = 0
            player1.baseball_bat = False
            player1.beretta_pistol = False
            player1.starting_knife = False
            player1.rocker_launcher = False
            player1.ak_47_rifle = False

    def save_game(self, player1: object):
        if not self.file_exists:
            print("data file does not exist. Creating new file.")

        with open(self.file, 'w') as user_data_file:
            user_data_file.write(json.dumps({'Balance': player1.user_balance,
                                             'Health': player1.user_health,
                                             'Merchant Luck': player1.merchant_luck,
                                             'Difficulty': player1.user_difficulty,
                                             'Starting Knife': player1.starting_knife,
                                             'Baseball Bat': player1.baseball_bat,
                                             'Beretta Pistol': player1.beretta_pistol,
                                             'AK 47 Rifle': player1.ak_47_rifle,
                                             'Rocket Missile Launcher': player1.rocker_launcher}))
            user_data_file.close()

import json
from os.path import exists as file_exists
from other.colors import print_green, print_yellow
from classes import Player


class Game_data:
    """
This class will offer loading and saving of game data for Zombie-Survival-Game.
    """

    def __init__(self):
        self.file = 'data.json'
        self.file_exists = bool(file_exists(self.file))

    def load_game(self, player1: object):
        if self.file_exists:
            with open(self.file, 'r') as user_data_file:
                user_data = json.load(user_data_file)
                player1.load_data(user_data)
                print_green('Saved data has been loaded successfully!\n')
        else:  # don't need to initialize values -- already initialized when class created
            print_yellow('No saved data found...\n')
            print_green('Starting a fresh game...\n')

    def save_game(self, player1: object):
        if not self.file_exists:
            print_yellow("No previous save! Creating new save...\n")

        with open(self.file, 'w') as user_data_file:
            json.dump(player1.get_data(), user_data_file)

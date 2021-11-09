#!/usr/bin/python3

# Created on 5/11/2021
from sys import exit
import webbrowser
from time import sleep
from random import randint
from other.colors import print_green, print_s
from classes import Player, Difficulty
from gamedata import GameData
from other.sounds_effects import GameSounds
from prettytable import PrettyTable
from choices import _player_choice, error_message
from gameprocess import *

player1 = Player()  # Player Instance
game_data = GameData()  # load/save functions Instance
sounds = GameSounds()  # audio that will be played Instance


# MENUS

def view_stats():
    """Prints the users current in game stats based upon a load file. Usage in Options"""
    player1.load_data(game_data.load_game())
    print_green('Your current in game stats will now be displayed below!\n\n', 1)

    myTable1 = PrettyTable(['Stat', 'Amount'])
    myTable1.add_row(['Health', player1.health])
    myTable1.add_row(['Balance', player1.balance])
    print(myTable1)
    weapons_owned = PrettyTable(['Weapons Owned'])
    weapons_owned.add_rows([[v[0]] for k, v in player1.weapon_dict.items() if v[2]])
    print(weapons_owned)
    myTable3 = PrettyTable(['Items Used'])
    myTable3.add_rows([[v[0]] for v in player1.consumables if v[2]])
    print(myTable3, '\n')


def open_github(print_text, website_append=''):
    """Open github in the users default web browser"""
    print_green(print_text)
    webbrowser.open_new(f'https://github.com/JordanLeich/Zombie-Survival-Game{website_append}')
    sleep(1)


def donation_opener(website):
    """Open a donation page in the users default web browser"""
    print_green("Opening PayPal Donation page...\n")
    webbrowser.open_new(website)
    sleep(2)


def list_achievements():
    for k, v in player1.achievement_list.items():
        if k[0] == '1':
            print(f'\nAll {k[1]} Achievements')
        print(f'{k[0]}. {v["name"]} - {v["desc"]}')
    sleep(5)


def options(choice=''):
    """UI for the user to view additional info or extra parts of this project"""
    choice_options = ['(1) View Stats',
                      '(2) Audio Options',
                      '(3) Achievements List',
                      '(4) Project Releases',
                      '(5) Credits',
                      '(6) Donate',
                      '(7) Main Menu',
                      '(8) Exit\n',
                      'Which choice would you like to pick:  '
                      ]
    while choice != '7' or choice != '8':
        choice = _player_choice([str(x) for x in range(1, 9)], choice_options)

        if choice == '1':
            view_stats()
        elif choice == '2':
            audio_options()
        elif choice == '3':
            list_achievements()
        elif choice == '4':
            open_github("Opening the latest stable release...\n", "/releases")
        elif choice == '5':
            open_github("Opening all contributors of this project...\n", "/graphs/contributors")
        elif choice == '6':
            donation_opener("https://www.paypal.com/donate/?business=8FGHU8Z4EJPME&no_recurring=0&currency_code=USD")
        elif choice == '7':
            return
        elif choice == '8':
            exit()


def game_menu():
    choice_options = ['(1) New Game',
                      '(2) Load Game',
                      '(3) Options',
                      '(4) Exit\n',
                      'Selection: ',
                      ]
    choice_dict = {'1': [game_intro, game, go_to_checkpoint],
                   '2': [load_or_save_data, game_intro, go_to_checkpoint],
                   '3': [options],
                   '4': [exit],
                   'unlock_all_cheat': [unlock_all_cheat, game]
                   }
    while True:
        print_green('Welcome to Zombie Survival Game!\n\nYour choices will allow you to Live or lead to Doom!\n')
        for item in choice_dict[_player_choice(list(choice_dict.keys()), choice_options)]:
            item()


def audio_options():
    choice_options = ['What would you like to set your volume level to (0 - 100) or exit: ']
    choices = [str(x) for x in range(101)]
    exit_choices = ['e', 'exit', 'c', 'close']
    choices.extend(exit_choices)
    while True:
        choice = _player_choice(choices, choice_options, len(exit_choices))
        if choice in exit_choices:
            break
        volume_level = int(choice) / 100
        sounds.set_volume(volume_level)
        sounds.zombie_attack_outside()
        print_s(f'Your current volume level is set at {choice}%\n', 1)


if __name__ == '__main__':
    game_menu()

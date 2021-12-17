#!/usr/bin/python3

# Created on 5/11/2021
import sys
import webbrowser
from PIL import Image
from classes import Player, Difficulty
from gamedata import GameData
from other.colors import print_blue
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
    myTable1.add_row(['XP Amount', player1.xp_amount])
    myTable1.add_row(['XP Level', player1.user_level])
    myTable1.add_row(['Total Kills', player1.total_kills])
    myTable1.add_row(['Player Deaths', player1.player_deaths])
    print(myTable1)
    weapons_owned = PrettyTable(['Weapons Owned'])
    weapons_owned.add_rows([[v[0]] for k, v in player1.weapon_dict.items() if v[2]])
    print(weapons_owned)
    myTable3 = PrettyTable(['Items Used'])
    myTable3.add_rows([[v[0]] for v in player1.consumables if v[2]])
    print(myTable3, '\n')


def open_github(print_text, website_append=''):
    """Open GitHub in the users default web browser"""
    print_green(print_text)
    webbrowser.open_new(f'https://github.com/JordanLeich/Zombie-Survival-Game{website_append}')
    sleep(1)


def donation_opener(website):
    """Open a donation page in the users default web browser"""
    print_green("Opening PayPal Donation page...\n")
    webbrowser.open_new(website)
    sleep(2)


def list_achievements():
    """Simply prints an entire list of all the achievements found in the classes file"""
    for k, v in player1.achievement_list.items():
        if k[0] == '1':
            print(f'\nAll {k[1]} Achievements')
        print(f'{k[0]}. {v["name"]} - {v["desc"]}')
    print()
    sleep(5)


def list_cheat_codes():
    """Simply prints an entire list of all the cheat codes"""
    print_yellow('--- Please keep in mind these cheat codes contain heavy spoilers ---\n', 1)
    print_yellow('--- Cheat codes must be entered at the main menu screen of the game ---\n', 1)
    print('''unlock_all_cheat
infinite_health_cheat
infinite_money_cheat\n''')
    sleep(3)


def concept_art():  # sourcery no-metrics
    """contains options and image openings for all concept art pieces"""
    print_yellow('--- Please keep in mind these images contain heavy spoilers ---\n', 1)
    choice_options = ['(1) Ch1 gas station',
                      '(2) Ch1 broken roads 1',
                      '(3) Ch1 broken roads 2',
                      '(4) Ch1 broken roads 3',
                      '(5) Ch2 woods',
                      '(6) Merchant 1',
                      '(7) Merchant 2',
                      '(8) Rookie protagonist 1',
                      '(9) Experienced protagonist 2',
                      '(10) Old man 1',
                      '(11) Sheriff 1',
                      '(12) Survivors 1',
                      '(13) Options Menu',
                      '(14) Exit\n',
                      'Which concept art would you like to view:  '
                      ]
    choice = _player_choice([str(x) for x in range(1, 15)], choice_options)

    if choice == '1':
        print_blue('Artwork by: Malek Mansour\n')
        image_path = 'images/concept art/ch1 gas station.jpg'
        img = Image.open(image_path)
        img.show(image_path)
        sleep(2)
        return concept_art()
    elif choice == '2':
        print_blue('Artwork by: Xavier Rault\n')
        image_path = 'images/concept art/ch1 broken roads 1.jpg'
        img = Image.open(image_path)
        img.show(image_path)
        sleep(2)
        return concept_art()
    elif choice == '3':
        print_blue('Artwork by: Xavier Rault\n')
        image_path = 'images/concept art/ch1 broken roads 2.jpg'
        img = Image.open(image_path)
        img.show(image_path)
        sleep(2)
        return concept_art()
    elif choice == '4':
        print_blue('Artwork by: Xavier Rault\n')
        image_path = 'images/concept art/ch1 broken roads 3.jpg'
        img = Image.open(image_path)
        img.show(image_path)
        sleep(2)
        return concept_art()
    elif choice == '5':
        print_blue('Artwork by: Marcus Marcussen\n')
        image_path = 'images/concept art/ch2 woods.jpg'
        img = Image.open(image_path)
        img.show(image_path)
        sleep(2)
        return concept_art()
    elif choice == '6':
        print_blue('Artwork by: Dark Souls\n')
        image_path = 'images/concept art/merchant 1.jpg'
        img = Image.open(image_path)
        img.show(image_path)
        sleep(2)
        return concept_art()
    elif choice == '7':
        print_blue('Artwork by: Dark Souls\n')
        image_path = 'images/concept art/merchant 2.jpg'
        img = Image.open(image_path)
        img.show(image_path)
        sleep(2)
        return concept_art()
    elif choice == '8':
        print_blue('Artwork by: Dmitry Pantiukhov\n')
        image_path = 'images/concept art/rookie protagonist 1.jpg'
        img = Image.open(image_path)
        img.show(image_path)
        sleep(2)
        return concept_art()
    elif choice == '9':
        print_blue('Artwork by: pngwing.com, Unknown creator\n')
        image_path = 'images/concept art/experienced protagonist 2.png'
        img = Image.open(image_path)
        img.show(image_path)
        sleep(2)
        return concept_art()
    elif choice == '10':
        print_blue('Artwork by: Dmitry Pantiukhov\n')
        image_path = 'images/concept art/old man 1.jpg'
        img = Image.open(image_path)
        img.show(image_path)
        sleep(2)
        return concept_art()
    elif choice == '11':
        print_blue('Artwork by: Dmitry Pantiukhov\n')
        image_path = 'images/concept art/sheriff 1.jpg'
        img = Image.open(image_path)
        img.show(image_path)
        sleep(2)
        return concept_art()
    elif choice == '12':
        print_blue('Artwork by: Gypsywine\n')
        image_path = 'images/concept art/survivors 1.png'
        img = Image.open(image_path)
        img.show(image_path)
        sleep(2)
        return concept_art()
    elif choice == '13':
        return
    elif choice == '14':
        exit()


def options(choice=''):
    """UI for the user to view additional info or extra parts of this project"""
    choice_options = ['(1) View Stats',
                      '(2) Audio Options',
                      '(3) Achievements List',
                      '(4) All Cheat Codes',
                      '(5) Project Releases',
                      '(6) Concept Art',
                      '(7) Credits',
                      '(8) Donate',
                      '(9) Main Menu',
                      '(10) Exit\n',
                      'Which choice would you like to pick:  '
                      ]
    while choice != '9' or choice != '10':
        choice = _player_choice([str(x) for x in range(1, 11)], choice_options)

        if choice == '1':
            view_stats()
        elif choice == '2':
            audio_options()
        elif choice == '3':
            list_achievements()
        elif choice == '4':
            list_cheat_codes()
        elif choice == '5':
            open_github("Opening the latest stable release...\n", "/releases")
        elif choice == '6':
            concept_art()
        elif choice == '7':
            open_github("Opening all contributors of this project...\n", "/graphs/contributors")
        elif choice == '8':
            donation_opener("https://www.paypal.com/donate/?business=8FGHU8Z4EJPME&no_recurring=0&currency_code=USD")
        elif choice == '9':
            return
        elif choice == '10':
            exit()


def game_menu():
    """handles the main menu UI options"""
    choice_options = ['(1) New Game',
                      '(2) Load Game',
                      '(3) Options',
                      '(4) Exit\n',
                      'Selection: ',
                      ]
    choice_dict = {'1': [difficulty, game, go_to_checkpoint],
                   '2': [load_or_save_data, difficulty, go_to_checkpoint],
                   '3': [options],
                   '4': [exit],
                   'unlock_all_cheat': [unlock_all_cheat, game],
                   'infinite_health_cheat': [infinite_health_cheat, game],
                   'infinite_money_cheat': [infinite_money_cheat, game]
                   }
    while True:
        sounds.intro_sounds()
        print_green('Welcome to Dead End!\n')
        print_sleep('This is a zombie survival game where you must make the best choices and '
                    'decisions possible in order to live.\nAs a survivor, you will encounter zombies, weapons, people, '
                    'and a merchant to buy from with an in-game currency.\nEvery decision you make has a cause and '
                    'effect while some lead you to fortune and others lead you to death.\n')
        for item in choice_dict[_player_choice(list(choice_dict.keys()), choice_options)]:
            item()


def audio_options():
    """allows the player to control or disable in game audio"""
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
        print_sleep(f'Your current volume level is set at {choice}%\n', 1)


if __name__ == '__main__':
    game_menu()

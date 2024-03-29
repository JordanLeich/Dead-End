""" This file holds all the main menus of the game and starts the game. """

# Created on 5/11/2021
import sys
import time
import webbrowser
from PIL import Image
from classes import Player, Difficulty
from gamedata import GameData
from other.colors import print_blue, print_green, print_sleep
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
    items_used = PrettyTable(['Items Used'])
    items_used.add_rows([[v[0]] for v in player1.consumables if v[2]])
    print(items_used, '\n')

def open_github(print_text, website_append=''):
    """Open GitHub in the users default web browser"""
    print_green(print_text)
    webbrowser.open_new(f'https://github.com/JordanLeich/Dead-End{website_append}')
    time.sleep(1)

def donation_opener():
    """Open a donation page in the users default web browser"""
    print_green("Opening PayPal Donation page...\n")
    webbrowser.open_new("https://www.paypal.com/donate/?business=8FGHU8Z4EJPME&no_recurring=0&currency_code=USD")
    time.sleep(2)

def list_achievements():
    """Simply prints an entire list of all the achievements found in the classes file"""
    for k, v in player1.achievement_list.items():
        if k[0] == '1':
            print(f'\nAll {k[1]} Achievements')
        print(f'{k[0]}. {v["name"]} - {v["desc"]}')
    print()
    time.sleep(5)

def list_cheat_codes():
    """Simply prints an entire list of all the cheat codes"""
    print_yellow('--- Please keep in mind these cheat codes contain heavy spoilers ---\n', 1)
    print_yellow('--- Cheat codes must be entered at the main menu screen of the game ---\n', 1)
    for x in ['unlock_all_cheat', 'infinite_health_cheat', 'infinite_money_cheat\n']:
        print(x)
    time.sleep(3)

def concept_art():  # sourcery no-metrics
    """contains options and image openings for all concept art pieces"""
    print_yellow('--- Please keep in mind these images contain heavy spoilers ---\n', 1)
    artwork_data = {
        '1': {'author': 'Malek Mansour', 'filename': 'chapter 1 gas station'},
        '2': {'author': 'Xavier Rault', 'filename': 'chapter 1 broken roads 1'},
        '3': {'author': 'Xavier Rault', 'filename': 'chapter 1 broken roads 2'},
        '4': {'author': 'Xavier Rault', 'filename': 'chapter 1 broken roads 3'},
        '5': {'author': 'Marcus Marcussen', 'filename': 'chapter 2 woods'},
        '6': {'author': 'Dark Souls', 'filename': 'merchant 1'},
        '7': {'author': 'Dark Souls', 'filename': 'merchant 2'},
        '8': {'author': 'Dmitry Pantiukhov', 'filename': 'rookie protagonist 1'},
        '9': {'author': 'pngwing.com, Unknown creator', 'filename': 'experienced protagonist 2'},
        '10': {'author': 'Dmitry Pantiukhov', 'filename': 'old man 1'},
        '11': {'author': 'Dmitry Pantiukhov', 'filename': 'sheriff 1'},
        '12': {'author': 'Gypsywine', 'filename': 'survivors 1'},
    }
    choice_options = [f"({c + 1}) {item[1]['filename'].capitalize()}" for c, item in enumerate(artwork_data.items())]
    choice_options.extend([f'({len(choice_options) + 1}) Options Menu', f'({len(choice_options) + 2}) Exit\n',
                           'Which concept art would you like to view:  '])

    choice = _player_choice([str(x) for x in range(1, len(choice_options) + 3)], choice_options)

    if choice == str(len(artwork_data) + 1):
        return
    elif choice == str(len(artwork_data) + 2):
        sys.exit()
    else:
        print_blue(f'Artwork by: {artwork_data[choice]["author"]}\n')
        image_path = f'images/concept art/{artwork_data[choice]["filename"]}.jpg'
        img = Image.open(image_path)
        img.show()
        time.sleep(2)
        return concept_art()

def game_version():
    """ Allows the user to see what version of the game they are currently playing on and upgrade their version if they are outdated. """
    current_game_version = 7.0
    latest_stable_release_version = 7.0

    if current_game_version == latest_stable_release_version:
        print_green(f'You are playing on version {current_game_version}. This version matches the most stable release of {latest_stable_release_version} on GitHub.\n')
    elif current_game_version < latest_stable_release_version:
        print_red(f'You are playing on version {current_game_version}. This version is outdated from the most stable release of {latest_stable_release_version} on GitHub. It is recommended to update to the latest release version on GitHub!\n')
        
        # Ask the user if they want to upgrade
        user_input = input("Do you want to upgrade to the latest version on GitHub? (yes/no): ")
        print()
        if user_input.lower() == 'yes':
            github_release_url = 'https://github.com/JordanLeich/Dead-End/releases'
            webbrowser.open(github_release_url)
            exit()
        else:
            print_yellow("Returning to outdated game...\n")
    elif current_game_version > latest_stable_release_version:
        print_yellow(f'You are playing on version {current_game_version}. This version is updated beyond the most stable release of {latest_stable_release_version} on GitHub. Beware of bugs that may occur!\n')
    else:
        print('Game version could not be found...\n')

def options(choice=''):
    """UI for the user to view additional info or extra parts of this project"""
    choice_options = ['(1) View Stats',
                      '(2) Audio Options',
                      '(3) Achievements List',
                      '(4) All Cheat Codes',
                      '(5) Game Version',
                      '(6) Project Releases',
                      '(7) Concept Art',
                      '(8) Time Played',
                      '(9) Credits',
                      '(10) Donate',
                      '(11) Main Menu',
                      '(12) Exit\n',
                      'Which choice would you like to pick:  '
                      ]
    choice_dict = {
        '1': [view_stats],
        '2': [audio_options],
        '3': [list_achievements],
        '4': [list_cheat_codes],
        '5': [game_version],
        '6': [open_github, "Opening the latest stable release...\n", "/releases"],
        '7': [concept_art],
        '8': [display_background_timer],
        '9': [open_github, "Opening all contributors of this project...\n", "/graphs/contributors"],
        '10': [donation_opener],
    }

    while choice != str(len(choice_options) - 2) or choice != str(len(choice_options) - 1):
        choice = _player_choice([str(x) for x in range(1, len(choice_options))], choice_options)

        if choice == str(len(choice_options) - 1):
            sys.exit()
        elif choice != str(len(choice_options) - 2):
            if len(choice_dict[choice]) > 1:
                choice_dict[choice][0](choice_dict[choice][1], choice_dict[choice][2])
            else:
                choice_dict[choice][0]()
        elif choice == str(len(choice_options) - 2):
            break

def horde_intro():
    print_green('Welcome to Horde Mode - A game mode set on defeating unlimited waves of zombies!\n')
    choice_options = ['(1) Select a difficulty',
                        '(2) Main menu',
                        '(3) Exit game\n',
                        'Select a choice: ',
                        ]
    choice_dict = {1: [horde_difficulty],
                   #2: [game_menu], # don't need as it creates an additional stack frame and will return to main menu anyway
                   3: [sys.exit],
                    #'unlock_all_cheat': [unlock_all_cheat, game],
                    #'infinite_health_cheat': [infinite_health_cheat, game],
                    #'infinite_money_cheat': [infinite_money_cheat, game]
                    }

    choices = [str(x) for x in range(1, len(choice_options))]
    choice = int(_player_choice(choices, choice_options))

    if choice == 1:
        horde_difficulty()
    elif choice == 3:
        sys.exit()

def horde_mode(horde_health):
    print_yellow('You will start with the 1997 Beretta Pistol.\n', 1.5)
    horde_total_kills = 0
    wave_number = 0
    player_alive = True
    beretta_pistol = True
    while player_alive:
        wave_number += 1
        print_yellow(f'Starting wave number: {wave_number}\n', 1)
        if wave_number % 5 == 0:  # award player cash for completing sets of waves
            wave_reward = (wave_number / 5) * 25
            player1.balance += wave_reward
            print_green(f'Due to reaching wave {wave_number}, you have earned {wave_reward} dollars!\n', 2)
        random_number_generator = randint(1, 3)
        if beretta_pistol:
            beretta_pistol_health_loss = randint(20, 30)
            zombies = (2 * random_number_generator) + 1
            print_red(f'A group of {zombies} zombies begin to head towards you and you begin to fight!\n', 1.5)
            horde_health -= beretta_pistol_health_loss
            if horde_health <= 0:
                player_alive = False
            horde_total_kills += zombies
            player1.total_kills += zombies
            print_green(f'You survived this wave while losing {beretta_pistol_health_loss} health.\n', 2)
            xp_level_system()
            time.sleep(1)
            print_green(f'Health remaining: {horde_health}\n', 1)
        else:
            print_red('No weapon has been acquired or set to True!\n', 2)
    print_red(f'You have died! You survived a total of {wave_number} waves.\n', 2)
    print_green(f'You now have killed a total of {player1.total_kills} zombies in both story and horde mode!\n', 1.5)
    # TODO add a save point here so that the players horde_total_kills saves for player.total_kills and horde xp saves for player1 xp.
    # game will auto return to main menu

def horde_difficulty():  # horde mode health and difficulty should be separate from story mode health and difficulty.
    """allows the user to select a difficulty for horde mode only."""
    print_sleep('--- All difficulty levels ---\n')
    print_green('(1) Easy - Start with 200 Health\n')
    print_yellow('(2) Medium - Start with 100 Health\n')
    print_red('(3) Hardcore - Start with 50 Health\n')
    difficulty_choice = int(input('Select a difficulty: '))
    print()
    sounds.difficulty_select_sound()

    if difficulty_choice == 1:
        horde_difficulty = 'Easy'
        horde_health = 200
    elif difficulty_choice == 2:
        horde_difficulty = 'Medium'
        horde_health = 100
    elif difficulty_choice == 3:
        horde_difficulty = 'Hardcore'
        horde_health = 50
    else:
        print_red('Error found!\n', 2)
    print_sleep(f'Difficulty set to {horde_difficulty} and Health set to {horde_health}.\n', 1.5)
    horde_mode(horde_health)

def game_menu():
    """handles the main menu UI options"""
    choice_options = ['(1) New Game',
                      '(2) Load Game',
                      '(3) Horde Mode',
                      '(4) Options',
                      '(5) Exit\n',
                      'Selection: ',
                      ]
    choice_dict = {'1': [difficulty, game, go_to_checkpoint],
                   '2': [load_or_save_data, difficulty, go_to_checkpoint],
                   '3': [horde_intro],
                   '4': [options],
                   '5': [False],
                   'unlock_all_cheat': [unlock_all_cheat, game],
                   'infinite_health_cheat': [infinite_health_cheat, game],
                   'infinite_money_cheat': [infinite_money_cheat, game]
                   }
    run_game = True
    while run_game:
        sounds.intro_sounds()
        print_green('Welcome to Dead End!\n')
        print_sleep('This is a zombie survival game where you must make the best choices and '
                    'decisions possible in order to live.\nAs a survivor, you will encounter zombies, weapons, people, '
                    'and a merchant to buy from with an in-game currency.\nEvery decision you make has a cause and '
                    'effect while some lead you to fortune and others lead you to death.\n')
        for item in (choice := choice_dict[_player_choice(list(choice_dict.keys()), choice_options)]):
            if choice == '3' and player1.chapter < 2:
                print_red('Sorry, Horde Mode unlocks after completing a chapter!\n', 2)  # TODO Needs to be fixed, player should not be able to access horde mode if their chapter number is set 1
                break
            if not item:
                run_game = False
            else:
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

def start_background_timer():
    """Acts as a background timer that starts as soon as the game is run."""
    player1.start_timer = time.time()  # Starts the background timer as soon as the game starts

def display_background_timer():
    """Acts as a background timer that starts as soon as the game is run."""
    end_timer = time.time()
    temporary_time_played = int((int(end_timer) - (int(player1.start_timer))) / 60)
    return print_blue(f'{temporary_time_played} Minutes played.\n', 1)

if __name__ == '__main__':
    start_background_timer()
    game_version()
    game_menu()

#!/usr/bin/python3

# Created on 5/11/2021
from sys import exit
import webbrowser
from time import sleep
from random import randint
from other.colors import print_green, print_yellow, print_red, print_s, print_health
from classes import Player, Difficulty
from gamedata import GameData
from other.sounds_effects import GameSounds

player1 = Player()  # Player Instance
game_data = GameData()  # load/save functions Instance
sounds = GameSounds()  # audio that will be played Instance

# constants:
ITEM_NUMBER = len(player1.weapon_dict)
CONSUMABLE_NUMBER = len(player1.consumables)
TOTAL_ITEMS = ITEM_NUMBER + CONSUMABLE_NUMBER
EXIT_MERCHANT_MENU = str(TOTAL_ITEMS)


def load_or_save_data():
    player1.load_data(game_data.load_game())


def game_intro_description():
    sounds.intro_sound()
    print_s('''This is a zombie survival game where you must make the best decisions possible in order to live.
As a survivor, you will encounter zombies, weapons, people, and a merchant to buy from with an
in-game currency. Every decision you make has a cause and effect while some lead you to fortune and others will 
lead you to death.\n''', 2.5)


def basement_area():
    print_s('You have reached the basement area.\n', 1)
    sounds.horror_sound_effects()
    print_s('''After living at your home for awhile now, you've had many supplies and broken utilities stored up in your basement.
Trailing behind you leads a lurking stench of odor containing of what smells like mold and rotten flesh.\n''', 1.5)
    choice_options = ['(1) Search around the basement (2) Forget about the basement and leave: ']
    choice = _player_choice([str(x) for x in range(1, 3)], choice_options)

    if choice == '1':
        print_s(
            'Amongst searching the basement, you stumble upon some spare money you forgot you had saved up in the basement.\n',
            1.5)
        sounds.good_luck()
        print_green(f'You found a total of ${player1.get_money()} dollars!\n', 1)
    elif choice == '2':
        sounds.wind_sound()
        print_s('''Upon leaving the basement, you head out into the outside area for a breath of fresh air after consuming 
the moldy and old smells of the basement.\n''', 2)


def unlock_all_cheat():
    sounds.good_luck()
    player1.health = 999999
    player1.balance = 999999
    player1.difficulty = Difficulty(0)
    for k, v in player1.weapon_dict.items():
        v[2] = True
    print_green('Unlock all cheats have been activated!\n', 2)
    checkpoint_save()


def game():
    if game_data.file_exists:
        sounds.difficulty_select_sound()
        print_green('Difficulty screen skipped due to saved data already existing...\n', 1)
        choice_options = ['Would you like to start a new game or continue with your saved data (new / continue): ']
        choice = _player_choice(['n', 'new', 'c', 'continue'], choice_options)

        if choice in ['n', 'new']:
            player1.balance = 0
            for k, v in player1.weapon_dict.items():
                v[2] = False
            difficulty()
            checkpoint_save()
        elif choice in ['c', 'continue']:
            print_green('Continuing game...\n', 1)
            go_to_checkpoint()
    else:
        difficulty()

    if player1.health <= 0:
        print_red('You currently have no health left...\n', 1)
        player1.check_point = f'{player1.check_point}bad'

    print('You have ended up in a small local town called Hinesville. This old town contains a population of about\n'
          'only 6000 people and holds only a Gas Station, Diner, and a Park. The current year is 1999 and you\n'
          'cannot wait to finally get on with your life and move somewhere more alive\n')
    sleep(2)
    choices = [str(x) for x in range(1, 4)]
    choices.append('unlock_all_cheat')
    choice_options = [
        'While sitting down in the living room of your house, you can either (1) Look around (2) Walk outside (3) Travel down the hidden door in the floor: ']
    choice = _player_choice(choices, choice_options)

    if choice == '1':
        print('You have decided to look around your apartment and decide to grab a concealed knife that you legally\n'
              'are allowed to carry in public areas just in case anything happens...\n')
        sleep(1)
        player1.weapon_dict['0'][2] = True  # no other way to find 
    elif choice == '2':
        sleep(1)
    elif choice == '3':
        sleep(1)
        basement_area()
    elif choice == 'unlock_all_cheat':
        unlock_all_cheat()
    checkpoint_save('1')


def merchant():  # sourcery no-metrics
    """Merchant randomly shows up, allowing the player to purchase weapons."""

    if player1.health <= 0:  # end game if no health
        print_red('You currently have no health left...\n', 1)
        player1.check_point = f'{player1.check_point}bad'

    if randint(1, 7) != 3:  # Random chance for player to interact with merchant
        return

    sounds.good_luck()
    print_green('Whoosh! The lucky merchant has appeared in-front of you...\n', 1)
    if player1.balance <= 0:
        print_yellow('Uh-Oh! You do not have enough money to buy anything... keep playing to acquire more money!\n', 1)
        return

    choices = ['b', 'buy', 'y', 'yes', 's', 'skip', 'n', 'no']
    choice_options = ['Would you like to buy from the merchant or skip past the merchant (buy / skip): ']
    choice = _player_choice(choices, choice_options)

    if choice in ['b', 'buy', 'y', 'yes']:
        buy_item = ''
        weapon_choices = [f"({k}) {v[0]} ({v[1]} Dollars)" for k, v in player1.weapon_dict.items() if k != '0']
        consumables = [f"({c + ITEM_NUMBER}) {v[0]} ({v[1]} Dollars)" for c, v in enumerate(player1.consumables)]
        while buy_item != EXIT_MERCHANT_MENU:
            print_green(f'Health: {player1.health}\n', 1)
            print_green(f'Balance: {player1.balance}\n', 1)
            choice_options = ['--- Merchants inventory ---']
            choice_options.extend(weapon_choices)
            choice_options.extend(consumables)
            choice_options.extend([f'({EXIT_MERCHANT_MENU}) Exit The Merchant Shop\n',
                                   'What would you like to buy: ',
                                   ])
            buy_item = _player_choice([str(x) for x in range(1, TOTAL_ITEMS + 1)], choice_options)

            if buy_item == EXIT_MERCHANT_MENU:
                print_s('The merchant bids you a farewell and good luck!\n', 1)
                break
            elif int(buy_item) >= ITEM_NUMBER:  # consumables
                consumable_index = int(buy_item) - ITEM_NUMBER
                if player1.balance > player1.consumables[consumable_index][1]:
                    player1.balance -= player1.consumables[consumable_index][1]
                    print_green(
                        f'You have used the {player1.consumables[consumable_index][0]}, giving you a bonus of {player1.consume(consumable_index)} health.\n',
                        2)
                else:
                    print_yellow('Sorry not enough available funds to purchase that item')
            elif player1.weapon_dict[buy_item][2]:
                sounds.bad_luck()
                print_yellow(f'{player1.weapon_dict[buy_item][0]} has already been purchased!\n', 1)
            elif player1.balance >= player1.weapon_dict[buy_item][1]:
                sounds.merchant_purchase_sound()
                player1.balance -= player1.weapon_dict[buy_item][1]
                player1.weapon_dict[buy_item][2] = True
                print_green(f'{player1.weapon_dict[buy_item][0]} has been purchased!\n', 1)
                if buy_item == '6':
                    print_green(
                        'As the Merchant hands you his own crafted spell, he tells you that you now wield true pain to foes whilst providing restoration to thine self.\n',
                        2.5)
            else:
                print_yellow('Sorry not enough available funds to purchase that item')
    elif choice in ['s', 'skip', 'n', 'no']:
        print_s('The merchant has been skipped but can be brought back later...\n', 1)


def continue_message():
    """Only for development purposes and has no impact on the game"""
    print_s('Continue here...', 3)
    exit()


# helper function for user_attack
def deep_index(lst, w):
    return [i for (i, sub) in enumerate(lst) if w in sub][0]


def user_attack(enemy='zombies'):
    """
This function is called whenever the players gets into a fight with zombies or humans. The logic is ordered in a way
so that the stronger weapon is used first instead of weaker weapons when attacking enemies.
    """
    choice_names = [v[0] for k, v in player1.weapon_dict.items() if v[2]]
    if not choice_names:  # no choice for them to make
        player1.health = 0
        print_red(
            'Due to not having any available weapons on you... You try to defend yourself...\nThe zombie overpowers you! Game Over!\n',
            3)
        player1.check_point = f'{player1.check_point}bad'
        return False

    choices = [str(c + 1) for c, _ in enumerate(choice_names)]
    choice_options = [f'({c + 1}) {v}' for c, v in enumerate(choice_names)]
    choice_options.extend(['\nWhich item would you like to use: '])
    choice = _player_choice(choices, choice_options)

    key = str(deep_index(list(player1.weapon_dict.values()), choice_names[int(choice) - 1]))

    if key == '6':
        print_green(
            f'You have used the Merchants Strange Spell and defeated the {enemy} without losing any health! Through the power of the Strange Spell, you gain {player1.get_health(10, 30)} health through its restoration casting!\n',
            3.5)
    else:  # print color based on user health
        lost_health = player1.use_item(key)
        if lost_health > player1.health:
            print_red(f'The {enemy} overpowered you. Losing all of your health...\n', 1)
            player1.check_point = f'{player1.check_point}bad'
            return False
        message = f'You have used the {player1.weapon_dict[key][0]} and defeated the {enemy} losing {lost_health} health!\n'
        if player1.health < 25:
            print_red(message, 2)
        elif player1.health < 50:
            print_yellow(message, 2)
        else:
            print_green(message, 2)
    return True  # attack successful


def gas_station():
    sounds.horror_sound_effects()
    print_s('You have entered the local Gas Station...\n', 1)

    print('From the front counter, you see a man who points his gun at you while you walk in! The man tells you to\n'
          'freeze but then notices that you are a survivor just like him... You both discuss and try to figure out\n'
          'what the hell is going on in this city and the man tells you that there has been a bacteria that can \n'
          'contaminated all meat supply chains across the world...\n')
    sleep(6)

    choice_options = [
        'You have the choice to either (1) Keep talking to the man (2) Ask the man for any supplies along your journey: ']
    user_choice = _player_choice([str(x) for x in range(1, 3)], choice_options)

    if user_choice == '1':
        print('As you keep talking to the man, he starts to tell you about his family and how they would always\n'
              'venture out to the park with his young daughter and son...\n')
        sleep(2)
        sounds.zombie_attack_inside()
        print_s(
            'Out of nowhere, a group of 3 zombies begin to bang on the glass door from which you entered in from...\n',
            2.5)
        sounds.zombie_attack_inside()
        print('While attempting to save you, the man fights off 2 zombies with his pump shotgun and get eaten alive '
              'while saying, RUN! but more zombies come to arise on you...\n')
        sleep(2.5)
        print_s('You decide to fight off the zombies in the will of your hopes for living...\n', 1.5)
        if not user_attack():
            return

        print_green('You have successfully defended off the zombies inside the gas station but it was most '
                    'unfortunate the man you found could not make it...\n', 2)
        choice_options = [
            'You have the choice to either (1) Search the all the bodies of zombies and the dead man (2) Head over to the local Diner: ']
        user_choice = _player_choice([str(x) for x in range(1, 3)], choice_options)

        if user_choice == '1':
            print_s(
                f'After search everybody in the gas station, you manage to find a total of {player1.get_money()} dollars and you then continue your way over to the local Diner...\n',
                2)
        checkpoint_save('2')
    elif user_choice == '2':
        sounds.good_luck()
        print(
            f'The man hands over some cash ({player1.get_money()} dollars) and tells you about a mysterious lurking salesman who would wonder around the town quite '
            'often... ')
        print('The man says that he has not seen him since the apocalypse has happened but keep the money on '
              'you in-case he shows...\n')
        sleep(2.5)
        sounds.wind_sound()
        print('You give thanks to the man and exit the local Gas Station and make your way down a tumbled and broken '
              'road... ')
        print('The gleaming fog and ashe outside is giving way to your vision and you see more and more '
              'unclear... Deep down inside... you know you must go on further...\n')
        sleep(3.5)
        checkpoint_save('2')


def outside_area():
    print_s('You make your way to the outside area...\n', 1)
    sounds.wind_sound()
    print('You instantly notice something is not right... a dark gloomy fog covers all of the town and you do not see\n'
          'a single friendly soul insight... You start to come to a conclusion about where everybody in the small\n'
          'town of Hinesville has went but nothing is making sense...\n')
    sleep(3.5)
    choice_options = ['You have the choice to either (1) Explore the Outside Area (2) Visit the local Gas Station: ']
    user_choice = _player_choice([str(x) for x in range(1, 3)], choice_options)

    if user_choice == '1':
        print('You decide to explore the outside area and along the way, you see a woman bleeding out on the ground\n'
              'with the shape of a man figure hovering over her...\n')
        sleep(2)
        sounds.zombie_attack_outside()
        print_s('Lone behold... the figure is eating the woman alive but you are too late to rescue her!\n', 1.5)
        choice_options = ['(1) Attack the zombie (2) Avoid the zombie and run to the local Gas Station: ']
        user_choice = _player_choice([str(x) for x in range(1, 3)], choice_options)

        if user_choice == '1':
            sounds.zombie_attack_outside()
            if not user_attack():
                return
            print_s(
                f'You then search the body of the zombie and decaying woman to find a total of {player1.get_money()} Dollars...\n',
                2)
            print_s('Finally, you get to make your way over to the local Gas Station...\n', 1.5)
        elif user_choice == '2':
            pass
    elif user_choice == '2':
        pass
    checkpoint_save('3')


def diner_area():
    sounds.horror_sound_effects()
    print_s('You have entered the local Diner...\n', 1)
    choice_options = [
        'You have the choice to either (1) Search inside the Diner Restaurant Area (2) head towards the Parkview Area: ']
    user_choice = _player_choice([str(x) for x in range(1, 3)], choice_options)

    if user_choice == '1':
        sounds.good_luck()
        print(
            f'After finishing up your entire search of the diner, you find a total of {player1.get_money()} dollars and ',
            f'you refresh up on some food and gain a total of {player1.get_health(5, 15)} health!\n')
        sleep(3)
        print('You also manage to find a bloody photograph on the ground and upon looking at the image, you see a '
              'familiar face...')
        print('You see the face of the man you met earlier at the local Gas Station taking a group family picture!\n')
        sleep(3)
        sounds.horror_sound_effects()
        print('Since you are finished exploring and searching the diner area, you proceed on your path to the '
              'parkview area...\n')
        sleep(3.5)
        checkpoint_save('4')
    elif user_choice == '2':
        sounds.zombie_attack_outside()
        print_red(
            'Upon leaving the diner area, you come across a group of about 5 zombies heading directly towards you!\n',
            1.5)
        if not user_attack():
            return

        print_green(
            'You have successfully defended off the zombies outside the local Diner... You will now head over to the Parkview Area\n',
            2)
        checkpoint_save('4')


def broken_roads_area():
    sounds.zombie_attack_outside()
    print('You have reached the broken roads area and managed to find a running vehicle but there are a group of '
          'about 3 zombies surrounding the vehicle... \nThe zombies begin to head directly towards you and you prepare '
          'to fight once more...\n')
    sleep(4.5)
    if not user_attack():
        return

    sounds.horror_sound_effects()
    print_green(
        'You have successfully fought off the zombies surrounding the running vehicle... You then enter the running vehicle...\nYou manage to put the vehicle into drive and you drive away into the sunrise...\n',
        4)
    checkpoint_save('6')


def parkview_area():
    sounds.horror_sound_effects()
    print_s('You have entered the parkview area...\n', 1)
    sounds.parkview_entrance()
    sleep(2.5)
    print_s('Upon arriving to the parkview area, you are still incapable of seeing very much ahead of yourself...\n',
            1.5)
    choice_options = ['You have the choice to either (1) Explore the Parkview Area (2) Explore onto the Broken Roads: ']
    user_choice = _player_choice([str(x) for x in range(1, 3)], choice_options)

    if user_choice == '1':
        print('Upon searching the Parkview Area... You come across a deranged man who is killing zombies left and '
              'right...\n')
        sleep(2)
        choice_options = ['You have the choice to either (1) Help the man (2) Kill the man: ']
        user_choice = _player_choice([str(x) for x in range(1, 3)], choice_options)

        if user_choice == '1':
            sounds.horror_sound_effects()
            print('In attempts of helping the man, he screams get the hell away from me, I will blow your head off! '
                  'You now prepare to fight him off!\n')
            sleep(2.5)
        elif user_choice == '2':
            sounds.bad_luck()

        if not user_attack('man'):  # attack same for both options - only difference is lead up to it
            sounds.bad_luck()
            print_red('The man has killed you and zombies start to feast on your dead decaying flesh...\n', 2)
            return

        print_green(
            f'You have successfully killed the man! Upon searching his body, you find a total of ${player1.get_money()}!\n',
            1)
        checkpoint_save('5')
        sounds.horror_sound_effects()
        print_s('You now decide to leave the Parkview Area...\n', 1.5)
        checkpoint_save('5')
    elif user_choice == '2':
        checkpoint_save('5')


def view_stats():
    """Prints the users current in game stats based upon a load file. Usage in Options"""
    player1.load_data(game_data.load_game())
    print_green('Your current in game stats will now be displayed below!\n', 1)
    print(f'Your health is {player1.health}\n')
    print_s(f'Your balance is ${player1.balance}\n', 2)


# helper function for player health setting and printing
def _difficulty_set_health():
    if player1.difficulty == Difficulty(1):
        player1.health = 200
    elif player1.difficulty == Difficulty(2):
        player1.health = 100
    elif player1.difficulty == Difficulty(3):
        player1.health = 50
    elif player1.difficulty == Difficulty(0):
        unlock_all_cheat()
    else:
        print('Since a saved difficulty value could not be found...')
        player1.health = 100
    print_health(player1.difficulty,
                 f'{player1.difficulty.name} mode has been selected, you will begin with {player1.health} health.\n',
                 1)


def difficulty():
    print_green('(1) Easy\n')
    print_yellow('(2) Medium\n')
    print_red('(3) Hardcore\n')
    choices = [str(x) for x in range(1, 4)]
    choices.append('unlock_all_cheat')
    choice_options = ['Select a difficulty: ']
    try:
        player1.difficulty = Difficulty(int(_player_choice(choices, choice_options)))
    except:
        player1.difficulty = Difficulty(0)  # unlock_all_cheat 

    sounds.difficulty_select_sound()
    _difficulty_set_health()


def restart():
    choices = ['y', 'yes', 'n', 'no']
    choice_options = ['Would you like to restart the game (yes / no): ']
    restart_choice = _player_choice(choices, choice_options)

    if restart_choice in ['y', 'yes']:
        _difficulty_set_health()
        player1.balance = 0
        for k, v in player1.weapon_dict.items():
            v[2] = False
        sounds.set_volume(0.05)
        print_green('Default stats have been loaded/saved and a new game will begin...\n', 1)
        player1.check_point = player1.check_point.replace('bad', '')  # load game from last checkpoint
        game_intro_description()
        game()
        go_to_checkpoint()
    elif restart_choice in ['n', 'no']:
        print_s('Ending game...', 1)
        exit()


def good_ending():
    sounds.good_luck()
    print_green('Congratulations, you have survived and reached the end of the horrors...\n', 1)
    print_green(f'You survived with a total of {player1.health} health left!\n', 1)
    restart()


def bad_ending():
    sounds.bad_ending()
    print_red('You have died and not reached the end of the horrors...\n', 1)
    restart()


def error_message(choices):  # to remove unlock_all_cheat as an option displayed for users
    if choices[-1] == 'unlock_all_cheat':
        print(f'Error choice must be one of: {", ".join(choices[:-1])}\n')
    else:
        print(f'Error choice must be one of: {", ".join(choices)}\n')


def checkpoint_save(checkpoint_name=''):
    player1.check_point = checkpoint_name
    game_data.save_game(player1.get_data())  # Sends player1 info to save file
    if player1.health <= 0:  # shouldn't really get to this point --> TODO
        print_red('Sorry you have no more health! You have lost the game!\n', 1)
        return  # restart()
    if checkpoint_name != '':  # remove checkpoint printing for ending + difficulty selected
        merchant()
        print_green('A checkpoint has been reached...\n', .5)
        print_green(f'Health: {player1.health}\n', 1)
        print_green(f'Balance: {player1.balance}\n', 1)

        choices = ['y', 'yes', 'n', 'no']
        choice_options = ['Would you like to exit the game (yes / no): ']
        exit_choice = _player_choice(choices, choice_options)
        if exit_choice in ['y', 'yes']:  # ask player if they would like to quit ~ returns to menu
            player1.check_point = f'{checkpoint_name}exit'


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


def options(choice=''):
    """UI for the user to view additional info or extra parts of this project"""
    while choice != '6' or choice != '7':
        choice_options = ['(1) View Stats',
                          '(2) Audio Options',
                          '(3) Project Releases',
                          '(4) Credits',
                          '(5) Donate',
                          '(6) Main Menu',
                          '(7) Exit\n',
                          'Which choice would you like to pick:  '
                          ]
        choice = _player_choice([str(x) for x in range(1, 8)], choice_options)

        if choice == '1':
            view_stats()
        elif choice == '2':
            audio_options()
        elif choice == '3':
            open_github("Opening the latest stable release...\n", "/releases")
        elif choice == '4':
            open_github("Opening all contributors of this project...\n", "/graphs/contributors")
        elif choice == '5':
            donation_opener("https://www.paypal.com/donate/?business=8FGHU8Z4EJPME&no_recurring=0&currency_code=USD")
        elif choice == '6':
            return
        elif choice == '7':
            exit()


def game_menu():
    choice_options = ['(1) New Game',
                      '(2) Load Game',
                      '(3) Options',
                      '(4) Exit\n',
                      'Selection: ',
                      ]
    choice_dict = {'1': [game_intro_description, game, go_to_checkpoint],
                   '2': [load_or_save_data, game_intro_description, game, go_to_checkpoint],
                   '3': [options],
                   '4': [exit],
                   'unlock_all_cheat': [unlock_all_cheat, game]
                   }
    while True:
        print_green('Welcome to Zombie Survival Game!\n\nYour choices will allow you to Live or lead to Doom!\n')
        for item in choice_dict[_player_choice(list(choice_dict.keys()), choice_options)]:
            item()


# helper function for player choices - handling errors and what paths to take next
def _player_choice(choices, choice_options: list, user_input=' ') -> str:
    while user_input.lower() not in choices:
        user_input = str(input('\n'.join(choice_options)))
        print_s('', 1)
        if user_input.lower() not in choices:
            error_message(choices)
        else:
            return user_input.lower()


def audio_options(volume_level=''):  # TODO: fix error message (prints every # between 1-100)
    choice_options = ['What would you like to set your volume level to (0 - 100) or exit: ']
    choices = [str(x) for x in range(101)]
    exit_choices = ['e', 'exit', 'c', 'close']
    choices.extend(exit_choices)
    while volume_level != 'exit':
        choice = _player_choice(choices, choice_options)
        if choice in exit_choices:
            break
        volume_level = int(choice) / 100
        sounds.set_volume(volume_level)
        sounds.zombie_attack_outside()
        print_s(f'Your current volume level is set at {sounds.volume_level}\n', 1)


def go_to_checkpoint():  # main program running movement to levels -- checkpoint when leaving area
    checkpoints = {'1': outside_area,
                   '2': diner_area,
                   '3': gas_station,
                   '4': parkview_area,
                   '5': broken_roads_area,
                   '6': good_ending,
                   '7': bad_ending,
                   }
    while 'exit' not in player1.check_point:
        if 'bad' in player1.check_point:
            checkpoints['7']()
        else:
            checkpoints[player1.check_point]()


if __name__ == '__main__':
    game_menu()

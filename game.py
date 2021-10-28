#!/usr/bin/python3

# Created on 5/11/2021

from sys import exit
import webbrowser
from time import sleep
from random import randint
from other.colors import print_green, print_yellow, print_red, print_s
from classes import Player
from gamedata import GameData
from other.sounds_effects import GameSounds

player1 = Player()  # Player Instance
game_data = GameData()  # load/save functions Instance
sounds = GameSounds()  # audio that will be played Instance


def load_or_save_data():
    game_data.load_game(player1)


def game_intro_description():
    sounds.intro_sound()
    print_s('''This is a zombie survival game where you must make the best decisions possible in order to live.
As a survivor, you will encounter zombies, weapons, people, and a merchant to buy from with an
in-game currency. Every decision you make has a cause and effect while some lead you to fortune and others will 
lead you to death.\n''', 2.5)
    game()


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
        continue_message()
    elif choice == '2':
        sounds.wind_sound()
        print_s('''Upon leaving the basement, you head out into the outside area for a breath of fresh air after consuming 
the moldy and old smells of the basement.\n''', 2)
        outside_area()


def unlock_all_cheat():
    sounds.good_luck()
    player1.user_health = 999999
    player1.user_balance = 999999
    player1.user_difficulty = 3
    player1.baseball_bat = True
    player1.beretta_pistol = True
    player1.starting_knife = True
    player1.rocket_launcher = True
    player1.ak_47_rifle = True
    player1.barrett_rifle = True
    player1.spell = True
    print_green('Unlock all cheats have been activated!\n', 2)
    checkpoint_save()
    game()


def game():
    if player1.user_difficulty in ['1', '2', '3']:
        sounds.difficulty_select_sound()
        print_green('Difficulty screen skipped due to saved data already existing...\n', 1)
        choice_options = ['Would you like to start a new game or continue with your saved data (new / continue): ']
        choice = _player_choice(['n', 'new', 'c', 'continue'], choice_options)

        if choice in ['n', 'new']:
            player1.user_health = 100
            player1.user_balance = 0
            player1.merchant_luck = 0
            player1.user_difficulty = 0
            player1.baseball_bat = False
            player1.beretta_pistol = False
            player1.starting_knife = False
            player1.rocket_launcher = False
            player1.ak_47_rifle = False
            player1.barrett_rifle = False
            player1.spell = False
            player1.check_point = ''
            print_green('Default stats have been loaded/saved and a new game will begin...\n', 1)
            checkpoint_save()
            game_intro_description()
        elif choice in ['c', 'continue']:
            print_green('Continuing game...\n', 1)
    else:
        difficulty()

    if player1.user_health <= 0:
        print_red('You currently have no health left...\n', 1)
        bad_ending()

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
        player1.starting_knife = True
        outside_area()
    elif choice == '2':
        sleep(1)
        outside_area()
    elif choice == '3':
        sleep(1)
        basement_area()
    elif choice == 'unlock_all_cheat':
        unlock_all_cheat()


def merchant():  # sourcery no-metrics

    if player1.user_health <= 0:
        print_red('You currently have no health left...\n', 1)
        bad_ending()

    player1.merchant_luck = randint(1, 7)

    if player1.merchant_luck == 3:
        sounds.good_luck()
        print_green('Whoosh! The lucky merchant has appeared in-front of you...\n', 1)

        if player1.user_balance <= 0:
            print_yellow('Uh-Oh! You do not have enough money to buy anything... keep playing to acquire more money!\n',
                         1)
        else:
            choices = ['b', 'buy', 'y', 'yes', 's', 'skip', 'n', 'no']
            choice_options = ['Would you like to buy from the merchant or skip past the merchant (buy / skip): ']
            choice = _player_choice(choices, choice_options)

            if choice in ['b', 'buy', 'y', 'yes']:
                print_green(f'Balance: {player1.user_balance}\n', 1)
                choice_options = ['--- Merchants inventory ---',
                                  '(1) Spiked Baseball Bat (5 Dollars)',
                                  '(2) 1997 Beretta Pistol (15 Dollars)',
                                  '(3) 1999 AK-47 Assault Rifle (25 Dollars)',
                                  '(4) 1999 Semi-automatic Barrett Sniper Rifle (60 Dollars)',
                                  '(5) Rocket Missile Launcher (100 Dollars)',
                                  '(6) The Merchants Strange Spell (125 Dollars)',
                                  '(7) Exit',
                                  'What would you like to buy: ',
                                  ]
                user_item_buy = _player_choice([str(x) for x in range(1, 8)], choice_options)

                if user_item_buy == '1' and player1.user_balance >= 5:
                    sounds.merchant_purchase_sound()
                    player1.user_balance -= 5
                    print_green('Spiked Baseball Bat has been purchased!\n', 1)
                    player1.baseball_bat = True
                elif user_item_buy == '2' and player1.user_balance >= 15:
                    sounds.merchant_purchase_sound()
                    player1.user_balance -= 15
                    print_green('1997 Beretta Pistol has been purchased!\n', 1)
                    player1.beretta_pistol = True
                elif user_item_buy == '3' and player1.user_balance >= 25:
                    sounds.merchant_purchase_sound()
                    print_green('1999 AK-47 Assault Rifle has been purchased!\n', 1)
                    player1.user_balance -= 25
                    player1.ak_47_rifle = True
                elif user_item_buy == '4' and player1.user_balance >= 60:
                    sounds.merchant_purchase_sound()
                    print_green('1999 Semi-automatic Barrett Sniper Rifle has been purchased!\n', 1)
                    player1.user_balance -= 60
                    player1.barrett_rifle = True
                elif user_item_buy == '5' and player1.user_balance >= 100:
                    sounds.merchant_purchase_sound()
                    print_green('Rocket Missile Launcher has been purchased!\n', 1)
                    player1.user_balance -= 100
                    player1.rocket_launcher = True
                elif user_item_buy == '6' and player1.user_balance >= 125:
                    sounds.merchant_purchase_sound()
                    print_green('The Merchants Strange Spell has been purchased!\n', 1)
                    sounds.good_luck()
                    print_green(
                        'As the Merchant hands you his own crafted spell, he tells you that you now wield true pain to foes whilst providing restoration to thine self.\n',
                        2.5)
                    player1.user_balance -= 125
                    player1.spell = True
                elif user_item_buy == '7':
                    print_s('The merchant has been skipped but can be brought back later...\n', 1)
            elif choice in ['s', 'skip', 'n', 'no']:
                print_s('The merchant has been skipped but can be brought back later...\n', 1)


def continue_message():
    """
This is purely only used for development and has no impact on the game
    """
    print_s('Continue here...', 3)
    exit()


def user_attack():
    """
This function is called whenever the players gets into a fight with zombies or humans. The logic is ordered in a way
so that the stronger weapon is used first instead of weaker weapons when attacking enemies.
    """
    if player1.spell:
        print_green(
            f'You have used the Merchants Strange Spell and defeated the zombies without losing any health! Through the power of the Strange Spell, you gain {player1.get_health(10, 30)} health through its restoration casting!\n',
            3.5)
    elif player1.rocket_launcher:
        print_green('You have used the Rocket Missile Launcher and defeated the zombies without losing any health!\n',
                    2)
    elif player1.barrett_rifle:
        print_green(
            f'You have used the Barrett Sniper Rifle and defeated the zombies with only losing {player1.lose_health(3, 10)} health!\n',
            2)
    elif player1.ak_47_rifle:
        print_green(
            f'You have used the AK-47 Rifle and defeated the zombies with only losing {player1.lose_health(10, 20)} health!\n',
            2)
    elif player1.beretta_pistol:
        print_green(
            f'You have used the Beretta Pistol and defeated the zombies with only losing {player1.lose_health(20, 30)} health!\n',
            2)
    elif player1.baseball_bat:
        print_yellow(
            f'You have used the Spiked Baseball Bat and defeated the zombies with losing {player1.lose_health(30, 40)} health!\n',
            2)
    elif player1.starting_knife:
        print_red(
            f'You have used the Starting Knife and defeated the zombies with losing {player1.lose_health(40, 45)} health!\n',
            2)
    else:
        player1.user_health = 0
        print_red(
            'Due to not having any available weapons or guns on you... You automatically cannot defend\nyourself and you have lost all of your health! Game Over!\n',
            3)
        bad_ending()


def gas_station():
    sounds.horror_sound_effects()
    print_s('You have entered the local Gas Station...\n', 1)

    checkpoint_save()

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
        user_attack()

        if player1.user_health > 0:
            print_green('You have successfully defended off the zombies inside the gas station but it was most '
                        'unfortunate the man you found could not make it...\n', 2)
            choice_options = [
                'You have the choice to either (1) Search the all the bodies of zombies and the dead man (2) Head over to the local Diner: ']
            user_choice = _player_choice([str(x) for x in range(1, 3)], choice_options)

            if user_choice == '1':
                print_s(
                    f'After search everybody in the gas station, you manage to find a total of {player1.get_money()} dollars and you then continue your way over to the local Diner...\n',
                    2)
                diner_area()
            elif user_choice == '2':
                diner_area()
        else:
            bad_ending()

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
        diner_area()


def outside_area():
    checkpoint_save()
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
            user_attack()
            print_s(
                f'You then search the body of the zombie and decaying woman to find a total of {player1.get_money()} Dollars...\n',
                2)
            print_s('Finally, you get to make your way over to the local Gas Station...\n', 1.5)
            gas_station()
        elif user_choice == '2':
            gas_station()
    elif user_choice == '2':
        gas_station()


def diner_area():
    sounds.horror_sound_effects()
    print_s('You have entered the local Diner...\n', 1)
    checkpoint_save()
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
        print('You see the face of the man you met earlier at the local Gas Station taking a group '
              'familiar face... \nYou see the face of the man you met earlier at the local Gas Station taking a group '
              'family picture!\n')
        sleep(3)
        sounds.horror_sound_effects()
        print('Since you are finished exploring and searching the diner area, you proceed on your path to the '
              'parkview area...\n')
        sleep(3.5)
        parkview_area()
    elif user_choice == '2':
        sounds.zombie_attack_outside()
        print_red(
            'Upon leaving the diner area, you come across a group of about 5 zombies heading directly towards you!\n',
            1.5)
        user_attack()

        if player1.user_health > 0:
            print_green(
                'You have successfully defended off the zombies outside the local Diner... You will now head over to the Parkview Area\n',
                2)
            parkview_area()

        else:
            bad_ending()


def broken_roads_area():
    sounds.zombie_attack_outside()
    print('You have reached the broken roads area and managed to find a running vehicle but there are a group of '
          'about 3 zombies surrounding the vehicle... \nThe zombies begin to head directly towards you and you prepare '
          'to fight once more...\n')
    sleep(4.5)
    user_attack()
    checkpoint_save()

    if player1.user_health > 0:
        sounds.horror_sound_effects()
        print_green(
            'You have successfully fought off the zombies surrounding the running vehicle... You then enter the running vehicle...\nYou manage to put the vehicle into drive and you drive away into the sunrise...\n',
            4)
        good_ending()
    else:
        bad_ending()


def parkview_area():
    sounds.horror_sound_effects()
    print_s('You have entered the parkview area...\n', 1)
    checkpoint_save()
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
            user_attack()

            if player1.user_health > 0:
                print_green(
                    f'You have successfully killed the man! Upon searching his body, you find a total of ${player1.get_money()}!\n',
                    1)
                checkpoint_save()
                sounds.horror_sound_effects()
                print_s('You now decide to leave the parkview area...\n', 1.5)
                broken_roads_area()
            else:
                sounds.bad_luck()
                print_red('The man has killed you and zombies start to feast on your dead decaying flesh...\n', 2)
                bad_ending()

        elif user_choice == '2':
            sounds.bad_luck()
            user_attack()

            if player1.user_health > 0:
                print_green(
                    f'You have successfully killed the man! Upon searching his body, you find a total of ${player1.get_money()}!\n',
                    1)
                checkpoint_save()
                sounds.horror_sound_effects()
                print_s('You now decide to leave the Parkview Area...\n', 1.5)
                broken_roads_area()
            else:
                sounds.bad_luck()
                print_red('The man has killed you and zombies start to feast on your dead decaying flesh...\n', 2)
                bad_ending()
    elif user_choice == '2':
        broken_roads_area()


def view_stats():
    """
Prints the users current in game stats based upon a load file
    """
    game_data.load_game(player1)
    print_green('Your current in game stats will now be displayed below!\n', 1)
    print(f'Your health is {player1.user_health}\n')
    print_s(f'Your balance is ${player1.user_balance}\n', 2)


def difficulty():
    print_green('(1) Easy\n')
    print_yellow('(2) Medium\n')
    print_red('(3) Hardcore\n')
    choices = [str(x) for x in range(1, 4)]
    choices.append('unlock_all_cheat')
    choice_options = ['Select a difficulty: ']
    player1.user_difficulty = _player_choice(choices, choice_options)

    sounds.difficulty_select_sound()
    if player1.user_difficulty == '1':
        print_green('Easy mode has been selected, you will begin with 200 health.\n', 1)
        player1.user_health = 200
    elif player1.user_difficulty == '2':
        print_yellow('Medium mode has been selected, you will begin with 100 health.\n', 1)
        player1.user_health = 100
    elif player1.user_difficulty == '3':
        print_red('Hardcore mode has been selected, you will begin with only 50 health.\n', 1)
        player1.user_health = 50
    elif player1.user_difficulty == 'unlock_all_cheat':
        unlock_all_cheat()


def restart():
    choices = ['y', 'yes', 'n', 'no']
    choice_options = ['Would you like to restart the game (yes / no): ']
    restart_choice = _player_choice(choices, choice_options)

    if restart_choice in ['y', 'yes']:
        if player1.user_difficulty == '1':
            print_green('You will begin with 200 health.\n')
            player1.user_health = 200
        elif player1.user_difficulty == '2':
            print_green('You will begin with 100 health.\n')
            player1.user_health = 100
        elif player1.user_difficulty == '3':
            print_green('You will begin with 50 health.\n')
            player1.user_health = 50
        else:
            print_yellow('Since a saved difficulty value could not be found... you will start with 100 health...\n', 1)
            player1.user_health = 100
        player1.user_balance = 0
        player1.merchant_luck = 0
        player1.baseball_bat = False
        player1.beretta_pistol = False
        player1.starting_knife = False
        player1.rocket_launcher = False
        player1.ak_47_rifle = False
        player1.barrett_rifle = False
        player1.spell = False
        sounds.set_volume(0.05)
        print_green('Default stats have been loaded/saved and a new game will begin...\n', 1)
        checkpoint_save()
        game_intro_description()
    elif restart_choice in ['n', 'no']:
        print_s('Ending game...', 1)
        exit()


def good_ending():
    sounds.good_luck()
    print_green('Congratulations, you have survived and reached the end of the horrors...\n', 1)
    print_green(f'You survived with a total of {player1.user_health} health left!\n', 1)
    checkpoint_save()
    restart()


def bad_ending():
    sounds.bad_ending()
    print_red('You have died and not reached the end of the horrors...\n', 1)
    checkpoint_save()
    restart()


def error_message(choices):
    if choices[-1] == 'unlock_all_cheat':
        print(f'Error choice must be one of: {", ".join(choices[:-1])}\n')
    else:
        print(f'Error choice must be one of: {", ".join(choices)}\n')


def checkpoint_save():
    if player1.user_health <= 0:
        print_red('You have reached a checkpoint and currently have no more health! You have lost the game!\n', 1)
        restart()
    merchant()
    print_green('A checkpoint has been reached...\n', .5)
    game_data.save_game(player1)  # Sends player1 info to save file
    print_green(f'Current Health: {player1.user_health}\n', 1)
    print_green(f'Current Balance: {player1.user_balance}\n', 1)
    if player1.user_difficulty == '1':
        print_green('Current Difficulty: Easy\n')
    elif player1.user_difficulty == '2':
        print_yellow('Current Difficulty: Medium\n')
    else:
        print_red('Current Difficulty: Hard\n', 1)


def open_github(print_text, website_append=''):
    """
    Open github in the users default web browser
    """
    print_green(print_text)
    webbrowser.open_new(f'https://github.com/JordanLeich/Zombie-Survival-Game{website_append}')
    sleep(1)


def donation_opener(website):
    """
    Open a donation page in the users default web browser
    """
    print_green("Opening PayPal Donation page...\n")
    webbrowser.open_new(website)
    sleep(2)


def options():
    """
Main hub UI for the user to view additional information or extra parts of this project such as donations and releases
    """
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
    choice_dict = {'1': [game_intro_description],
                   '2': [load_or_save_data, game_intro_description],
                   '3': [options],
                   '4': [exit],
                   'unlock_all_cheat': [unlock_all_cheat]
                   }
    print_green('Welcome to Zombie Survival Game!\n\nYour choices will allow you to Live or lead to Doom!\n')
    for item in choice_dict[_player_choice(choice_dict, choice_options)]:
        item()


# helper function for player choices - handling errors + what paths to take next
def _player_choice(choices, choice_options: list) -> str:
    user_input = ' '
    while user_input.lower() not in choices:
        user_input = str(input('\n'.join(choice_options)))
        print_s('', 1)
        if user_input.lower() not in choices:
            error_message(choices)
        else:
            return user_input.lower()
    ''' # idea to make commands as dictionary that will play through? what benefits over just playing commands? None that I am aware of 
    for item in choice_dict[_player_choice(choice_dict, choice_options)]:
        if isinstance(item, list):
            _print_choice(item)
        else:
            item()
    '''


def audio_options():  # sourcery skip: remove-zero-from-range
    choice_options = ['What would you like to set your volume level to (0 - 100): ']
    volume_level = int(_player_choice([str(x) for x in range(0, 101)], choice_options)) / 100
    sounds.set_volume(volume_level)
    print_s(f'Your current volume level is set at {sounds.volume_level}\n', 1)
    options()


if __name__ == '__main__':
    game_menu()

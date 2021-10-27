#!/usr/bin/python3

# Created on 5/11/2021

import sys
import webbrowser
from time import sleep
from random import randint
# files
from other import sounds_effects
from other.colors import print_green, print_yellow, print_red
from classes import Player
from gamedata import Game_data

player1 = Player()
game_data = Game_data()


def load_or_save_data():
    game_data.load_game(player1)


def game_intro_description():
    sounds_effects.intro_sound()
    print('''This is a zombie survival game where you must make the best decisions possible in order to live.
As a survivor, you will encounter zombies, weapons, people, and a merchant to buy from with an
in-game currency. Every decision you make has a cause and effect while some lead you to fortune and others will 
lead you to death.\n''')
    sleep(2.5)
    game()


def basement_area():
    continue_message()
    # TODO: continue story here with the basement function


def game():
    if player1.user_difficulty in [1, 2, 3]:
        sounds_effects.difficulty_select_sound()
        print_green('Difficulty screen skipped due to saved data already existing...\n')
        sleep(1)
        choice = str(input('Would you like to restart the game from scratch or continue with your saved data '
                           '(restart / continue): '))
        print()
        sleep(1)
        if choice.lower() in ['r', 'restart']:
            player1.user_health = 100
            player1.user_balance = 0
            player1.merchant_luck = 0
            player1.user_difficulty = 0
            player1.baseball_bat = False
            player1.beretta_pistol = False
            player1.starting_knife = False
            player1.rocket_launcher = False
            player1.ak_47_rifle = False
            player1.volume_level = 0.0
            player1.check_point = ''
            print_green('Default stats have been loaded/saved and a new game will begin...\n')
            sleep(1)
            checkpoint_save()
            game_intro_description()
        elif choice.lower() in ['c', 'continue']:
            print_green('Continuing game...\n')
            sleep(1)
        else:
            error_message()
    else:
        difficulty()

    if player1.user_health <= 0:
        print_red('You currently have no health left...\n')
        sleep(1)
        bad_ending()

    print('You have ended up in a small local town called Hinesville. This old town contains a population of about\n'
          'only 6000 people and holds only a Gas Station, Diner, and a Park. The current year is 1999 and you\n'
          'cannot wait to finally get on with your life and move somewhere more alive\n')
    sleep(2)
    user_choice = int(input('While sitting down in your living room apartment, you can either (1) Look around '
                            '(2) Walk outside (3) Travel down the hidden door in the floor: '))
    print()
    sleep(1)

    if user_choice == 1:
        print('You have decided to look around your apartment and decide to grab a concealed knife that you legally\n'
              'are allowed to carry in public areas just in case anything happens...\n')
        sleep(1)
        player1.starting_knife = True
        outside_area()
    elif user_choice == 2:
        sleep(1)
        outside_area()
    elif user_choice == 3:
        sleep(1)
        basement_area()
    else:
        error_message()


def merchant():  # sourcery no-metrics

    if player1.user_health <= 0:
        print_red('You currently have no health left...\n')
        sleep(1)
        bad_ending()

    player1.merchant_luck = randint(1, 7)

    if player1.merchant_luck == 3:
        sounds_effects.good_luck()
        print_green('Whoosh! The lucky merchant has appeared in-front of you...\n')
        sleep(1)

        if player1.user_balance <= 0:
            print_yellow('Uh-Oh! You do not have enough money to buy anything... keep playing to acquire more money!\n')
            sleep(1)
        else:
            user_choice = str(input('Would you like to buy from the merchant or skip past the merchant (buy / skip): '))
            print()
            sleep(1)

            if user_choice.lower() in ['b', 'buy', 'y', 'yes']:
                print_green(f'Balance: {player1.user_balance}\n')
                sleep(1)
                user_item_buy = int(input('''--- Merchants inventory ---
(1) Spiked Baseball Bat (5 Dollars)
(2) 1997 Beretta Pistol (15 Dollars)
(3) 1999 AK-47 Assault Rifle (25 Dollars)
(4) Rocket Missile Launcher (100 Dollars)
(5) Exit

What would you like to buy: '''))
                print()
                sleep(1)

                if user_item_buy == 1 and player1.user_balance >= 5:
                    sounds_effects.merchant_purchase_sound()
                    player1.user_balance -= 5
                    print_green('Spiked Baseball Bat has been purchased!\n')
                    player1.baseball_bat = True
                    sleep(1)
                elif user_item_buy == 2 and player1.user_balance >= 15:
                    sounds_effects.merchant_purchase_sound()
                    player1.user_balance -= 15
                    print_green('1997 Beretta Pistol has been purchased!\n')
                    player1.beretta_pistol = True
                    sleep(1)
                elif user_item_buy == 3 and player1.user_balance >= 25:
                    sounds_effects.merchant_purchase_sound()
                    print_green('1999 AK-47 Assault Rifle has been purchased!\n')
                    player1.user_balance -= 25
                    player1.ak_47_rifle = True
                    sleep(1)
                elif user_item_buy == 4 and player1.user_balance >= 100:
                    sounds_effects.merchant_purchase_sound()
                    print_green('Rocket Missile Launcher has been purchased!\n')
                    player1.user_balance -= 100
                    player1.rocket_launcher = True
                    sleep(1)
                elif user_item_buy == 5:
                    print_green('Purchasing from the merchant has been skipped...\n')
                    sleep(1)
                else:
                    error_message()

            elif user_choice.lower() in ['s', 'sell', 'n', 'no']:
                print('The merchant has been skipped but can be brought back later...\n')
                sleep(1)
            else:
                error_message()


def continue_message():
    """
This is purely only used for development and has no impact on the game
    """
    print('Continue here...')
    sleep(3)
    sys.exit()


def user_attack():
    if player1.rocket_launcher:
        player1.user_health -= 0
        print_green('You have used the rocket missile launcher and defeated the zombies without losing any health!\n')
        sleep(2)
    elif player1.ak_47_rifle:
        player1.user_health -= 10
        print_green('You have used the ak-47 rifle and defeated the zombies with only losing 10 health!\n')
        sleep(2)
    elif player1.beretta_pistol:
        player1.user_health -= 25
        print_green('You have used the beretta pistol and defeated the zombies with only losing 25 health!\n')
        sleep(2)
    elif player1.baseball_bat:
        player1.user_health -= 35
        print_green('You have used the baseball bat and defeated the zombies with losing 35 health!\n')
        sleep(2)
    elif player1.starting_knife:
        player1.user_health -= 45
        print_green('You have used the starting knife and defeated the zombies with losing 45 health!\n')
        sleep(2)
    else:
        player1.user_health = 0
        print_red(
            'Due to not having any available weapons or guns on you... You automatically cannot defend\nyourself and you have lost all of your health!\n')
        sleep(2)
        bad_ending()


def gas_station():
    sounds_effects.horror_sound_effects()
    print('You have entered the local Gas Station...\n')
    sleep(1)

    checkpoint_save()

    print('From the front counter, you see a man who points his gun at you while you walk in! The man tells you to\n'
          'freeze but then notices that you are a survivor just like him... You both discuss and try to figure out\n'
          'what the hell is going on in this city and the man tells you that there has been a bacteria that can \n'
          'contaminated all meat supply chains across the world...\n')
    sleep(5)
    user_choice = int(input('You have the choice to either (1) Keep talking to the man (2) Ask the man for any '
                            'supplies along your journey: '))
    print()
    sleep(1)

    if user_choice == 1:
        print('As you keep talking to the man, he starts to tell you about his family and how they would always\n'
              'venture out to the park with his young daughter and son...\n')
        sleep(2)
        sounds_effects.zombie_attack_inside()
        print('Out of nowhere, a group of 3 zombies begin to bang on the glass door from which you entered in from...'
              '\n')
        sleep(2.5)
        sounds_effects.zombie_attack_inside()
        print('While attempting to save you, the man fights off 2 zombies with his pump shotgun and get eaten alive '
              'while saying, RUN! but more zombies come to arise on you...\n')
        sleep(2.5)
        print('You decide to fight off the zombies in the will of your hopes for living...\n')
        sleep(1.5)
        user_attack()

        if player1.user_health > 0:
            print_green('You have successfully defended off the zombies inside the gas station but it was most '
                        'unfortunate the man you found could not make it...\n')
            sleep(2)
            user_choice = int(input('You have the choice to either (1) Search the all the bodies of zombies and the '
                                    'dead man (2) Head over to the local Diner: '))
            print()
            sleep(1)

            if user_choice == 1:
                random_money = randint(5, 30)
                print('After search everybody in the gas station, you manage to find a total of', random_money,
                      'dollars and you then continue your way over to the local Diner...\n')
                player1.user_balance += random_money
                sleep(2)
                diner_area()
            elif user_choice == 2:
                diner_area()
            else:
                error_message()

        else:
            bad_ending()

    elif user_choice == 2:
        sounds_effects.good_luck()
        random_money = randint(5, 30)
        print('The man hands over some cash (' + str(random_money),
              'dollars) and tells you about a mysterious lurking salesman who would wonder around the town quite '
              'often... ')
        print('The man says that he has not seen him since the apocalypse has happened but keep the money on '
              'you in-case he shows...\n')

        player1.user_balance += random_money
        sleep(2.5)
        sounds_effects.wind_sound()
        print('You give thanks to the man and exit the local Gas Station and make your way down a tumbled and broken '
              'road... ')
        print('The gleaming fog and ashe outside is giving way to your vision and you see more and more '
              'unclear... Deep down inside... you know you must go on further...\n')
        sleep(3.5)
        diner_area()
    else:
        error_message()


def outside_area():
    print('You make your way to the outside area...\n')
    sleep(1)
    sounds_effects.wind_sound()
    print('You instantly notice something is not right... a dark gloomy fog covers all of the town and you do not see '
          'a single friendly soul insight... ')
    print('You start to come to a conclusion about where everybody in the small town of Hinesville has went but '
          'nothing is making sense...\n')
    print('You instantly notice something is not right... a dark gloomy fog covers all of the town and you do not see\n'
          'a single friendly soul insight... You start to come to a conclusion about where everybody in the small\n'
          'town of Hinesville has went but nothing is making sense...\n')
    sleep(3.5)
    user_choice = int(input('You have the choice to either (1) Explore the Outside Area (2) Visit the local Gas '
                            'Station: '))
    print()
    sleep(1)

    if user_choice == 1:
        print('You decide to explore the outside area and along the way, you see a woman bleeding out on the ground '
              'with the shape of a man figure hovering over her...\n')
        sleep(2)
        sounds_effects.zombie_attack_outside()
        print('Lone behold... the figure is eating the woman alive but you are too late to rescue her!\n')
        sleep(1.5)
        user_choice = int(input('(1) Attack the zombie or (2) Avoid the zombie and run to the local Gas Station: '))
        print()
        sleep(1)

        if user_choice == 1 and player1.starting_knife:
            sounds_effects.zombie_attack_outside()
            random_money = randint(5, 30)
            print('You attacked the zombie with the knife you found earlier and killed the zombie while losing 15 '
                  'health... \nYou search the body of the zombie and woman to find a total of', random_money,
                  'Dollars...\n')
            player1.user_balance += random_money
            player1.user_health -= 15
            sleep(2)
            print('You then finally get to make your way over to the local Gas Station...\n')
            sleep(1.5)
            gas_station()

        elif user_choice == 2:
            gas_station()
        else:
            error_message()

    elif user_choice == 2:
        gas_station()
    else:
        error_message()


def diner_area():
    sounds_effects.horror_sound_effects()
    print('You have entered the local Diner...\n')
    sleep(1)
    checkpoint_save()
    user_choice = int(input('You have the choice to either (1) Search inside the Diner Restaurant Area (2) '
                            'head towards the Parkview Area: '))
    print()
    sleep(1)

    if user_choice == 1:
        sounds_effects.good_luck()
        random_money = randint(5, 30)
        random_health = randint(5, 15)
        print('After finishing up your entire search of the diner, you find a total of', random_money, 'dollars and '
                                                                                                       'you refresh '
                                                                                                       'up on some '
                                                                                                       'food and gain '
                                                                                                       'a total of',
              random_health, 'health!\n')
        player1.user_balance += random_money
        player1.user_health += random_health
        sleep(3)
        print('You also manage to find a bloody photograph on the ground and upon looking at the image, you see a '
              'familiar face...')
        print('You see the face of the man you met earlier at the local Gas Station taking a group '
              'familiar face... \nYou see the face of the man you met earlier at the local Gas Station taking a group '
              'family picture!\n')
        sleep(3)
        sounds_effects.horror_sound_effects()
        print('Since you are finished exploring and searching the diner area, you proceed on your path to the '
              'parkview area...\n')
        sleep(3.5)
        parkview_area()

    elif user_choice == 2:
        sounds_effects.zombie_attack_outside()
        print_red(
            'Upon leaving the diner area, you come across a group of about 5 zombies heading directly towards you!\n')
        sleep(1.5)
        user_attack()

        if player1.user_health > 0:
            print_green(
                'You have successfully defended off the zombies outside the local Diner... You will now head over to the Parkview Area\n')
            sleep(2)
            parkview_area()

        else:
            bad_ending()

    else:
        error_message()


def broken_roads_area():
    sounds_effects.zombie_attack_outside()
    print('You have reached the broken roads area and managed to find a running vehicle but there are a group of '
          'about 3 zombies surrounding the vehicle... \nThe zombies begin to head directly towards you and you prepare '
          'to fight once more...\n')
    sleep(4.5)
    user_attack()
    checkpoint_save()

    if player1.user_health > 0:
        sounds_effects.horror_sound_effects()
        print_green(
            'You have successfully fought off the zombies surrounding the running vehicle... You then enter the running vehicle... The manage to put the vehicle into drive and you drive away into the sunrise...\n')
        sleep(4)
        good_ending()
    else:
        bad_ending()


def parkview_area():
    sounds_effects.horror_sound_effects()
    print('You have entered the parkview area...\n')
    sleep(1)
    checkpoint_save()
    sounds_effects.parkview_entrance()
    sleep(2.5)
    print('Upon arriving to the parkview area, you are still incapable of seeing very much ahead of yourself...\n')
    sleep(1.5)
    user_choice = int(input('You have the choice to either (1) Explore the Parkview Area (2) Explore onto the Broken '
                            'Roads: '))
    print()
    sleep(1)

    if user_choice == 1:
        print('Upon searching the Parkview Area... You come across a deranged man who is killing zombies left and '
              'right...\n')
        sleep(2)
        user_choice = int(input('You have the choice to either (1) Help the man (2) Kill the man: '))
        print()
        sleep(1)

        if user_choice == 1:
            sounds_effects.horror_sound_effects()
            print('In attempts of helping the man, he screams get the hell away from me, I will blow your head off! '
                  'You now prepare to fight him off!\n')
            sleep(2.5)
            user_attack()

            if player1.user_health > 0:
                random_money = randint(5, 30)
                print_green(
                    f'You have successfully killed the man! Upon searching his body, you find a total of ${random_money}!\n')
                player1.user_balance += random_money
                sleep(1)
                checkpoint_save()
                sounds_effects.horror_sound_effects()
                print('You now decide to leave the parkview area...\n')
                sleep(1.5)
                broken_roads_area()

            else:
                sounds_effects.bad_luck()
                print_red('The man has killed you and zombies start to feast on your dead decaying flesh...\n')
                sleep(2)
                bad_ending()

        elif user_choice == 2:
            sounds_effects.bad_luck()
            user_attack()

            if player1.user_health > 0:
                random_money = randint(5, 30)
                print_green(
                    f'You have successfully killed the man! Upon searching his body, you find a total of ${random_money}!\n')
                player1.user_balance += random_money
                sleep(1)
                checkpoint_save()
                sounds_effects.horror_sound_effects()
                print('You now decide to leave the Parkview Area...\n')
                sleep(1.5)
                broken_roads_area()

            else:
                sounds_effects.bad_luck()
                print_red('The man has killed you and zombies start to feast on your dead decaying flesh...\n')
                sleep(2)
                bad_ending()

    elif user_choice == 2:
        broken_roads_area()
    else:
        error_message()


def difficulty():
    print_green('(1) Easy\n')
    print_yellow('(2) Medium\n')
    print_red('(3) Hardcore\n')
    player1.user_difficulty = int(input('Select a difficulty: '))
    print()
    sleep(1)
    sounds_effects.difficulty_select_sound()

    if player1.user_difficulty == 1:
        print_green('Easy mode has been selected, you will begin with 200 health.\n')
        player1.user_health = 200
        sleep(1)
    elif player1.user_difficulty == 2:
        print_yellow('Medium mode has been selected, you will begin with 100 health.\n')
        player1.user_health = 100
        sleep(1)
    elif player1.user_difficulty == 3:
        print_red('Hardcore mode has been selected, you will begin with only 50 health.\n')
        player1.user_health = 50
        sleep(1)
    else:
        error_message()


def restart():
    restart_choice = str(input('Would you like to restart the game (yes / no): '))
    print()

    if restart_choice.lower() in ['y', 'yes']:
        if player1.user_difficulty == 1:
            print_green('You will begin with 200 health.\n')
            player1.user_health = 200
        elif player1.user_difficulty == 2:
            print_green('You will begin with 100 health.\n')
            player1.user_health = 100
        elif player1.user_difficulty == 3:
            print_green('You will begin with 50 health.\n')
            player1.user_health = 50
        else:
            print_yellow('Since a saved difficulty value could not be found... you will start with 100 health...\n')
            sleep(1)
            player1.user_health = 100
        player1.user_balance = 0
        player1.merchant_luck = 0
        player1.baseball_bat = False
        player1.beretta_pistol = False
        player1.starting_knife = False
        player1.rocket_launcher = False
        player1.ak_47_rifle = False
        player1.volume_level = 0.0
        print_green('Default stats have been loaded/saved and a new game will begin...\n')
        sleep(1)
        checkpoint_save()
        game_intro_description()
    elif restart_choice.lower() in ['n', 'no']:
        print('Ending game...')
        sleep(1)
        sys.exit()
    else:
        error_message()


def good_ending():
    sounds_effects.good_luck()
    print_green('Congratulations, you have survived and reached the end of the horrors...\n')
    sleep(1)
    print_green(f'You survived with a total of {player1.user_health} health left!\n')
    sleep(1)
    checkpoint_save()
    restart()


def bad_ending():
    sounds_effects.bad_ending()
    print_red('You have died and not reached the end of the horrors...\n')
    sleep(1)
    checkpoint_save()
    restart()


def error_message():
    sleep(1)
    sounds_effects.bad_luck()
    print_red('An error has been found... restarting game...\n')
    sleep(2)
    game()


def checkpoint_save():
    if player1.user_health <= 0:
        print_red('You have reached a checkpoint and currently have no more health! You have lost the game!\n')
        sleep(1)
        restart()
    merchant()
    print_green('A checkpoint has been reached...\n')
    sleep(.5)
    game_data.save_game(player1)  # Sends player1 info to save file
    print_green(f'Current Health: {player1.user_health}\n')
    sleep(1)
    print_green(f'Current Balance: {player1.user_balance}\n')
    sleep(1)
    if player1.user_difficulty == 1:
        print_green('Current Difficulty: Easy\n')
    elif player1.user_difficulty == 2:
        print_yellow('Current Difficulty: Medium\n')
    else:
        print_red('Current Difficulty: Hard\n')
    sleep(1)


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
    while True:
        print("(1) View Stats")
        print("(2) Audio")
        print("(3) Project Releases")
        print("(4) Credits")
        print("(5) Donate")
        print("(6) Main Menu")
        print("(7) Exit\n")
        choice = input("Which choice would you like to pick:  ")
        print()
        sleep(.5)

        if choice == '1':
            continue_message()
            # view_stats() TODO Add a view stats function
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
            sys.exit()
        else:
            print_red("Please select a number from 1 - 8.\n")


def game_menu():
    while True:
        print_green('Welcome to Zombie Survival Game!\n\nYour choices will allow you to Live or lead to Doom!\n')
        print('(1) New Game')
        print('(2) Load Game')
        print('(3) Options')
        print('(4) Exit\n')
        user_input = str(input('Selection: '))
        print()
        sleep(.5)

        if user_input not in ['1', '2', '3', '4']:
            print('That is not a valid input. Please select a number between (1-4)')
        elif user_input == '1':
            game_intro_description()
        elif user_input == '2':
            load_or_save_data()
            game_intro_description()
        elif user_input == '3':
            options()
        else:
            sys.exit()


def audio_options():
    # sourcery skip: merge-duplicate-blocks, remove-redundant-if, remove-unnecessary-else, swap-if-else-branches
    volume_level = float(input('What would you like to set your volume level to (0.05 is default, 1.0 is the max and '
                               '0.0 is muted): '))
    print()
    sleep(1)
    if volume_level < 0.0:
        print_red('Please only select a volume level between 0.0 and 1.0!\n')
        sleep(1)
    elif volume_level > 1.0:
        print_red('Please only select a volume level between 0.0 and 1.0!\n')
        sleep(1)
    else:
        player1.volume_level = volume_level
        print('Your current volume level is set at', player1.volume_level, '\n')
        sleep(1)
        return player1.volume_level


if __name__ == '__main__':
    game_menu()

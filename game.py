#!/usr/bin/python3

# Created on 5/11/2021

# Imports
import sys
import time
import random

from other import colors, sounds_effects
from classes import Player
from time import sleep
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
    # TODO: continue story here with the basement function
    print('finish story here...\n')
    time.sleep(5)
    sys.exit()


def game():
    try:
        with open('data.json', 'r'):
            sounds_effects.difficulty_select_sound()
            print(colors.green + 'Difficulty screen skipped due to saved data already existing...\n', colors.reset)
            sleep(1)
            choice = str(input('Would you like to restart the game from scratch or continue with your saved data '
                               '(restart / continue): '))
            print()
            sleep(1)
            if choice.lower() in ['r', 'restart']:
                player1.user_health = 100
                player1.user_balance = 0
                player1.merchant_luck = 0
                player1.baseball_bat = False
                player1.beretta_pistol = False
                player1.starting_knife = False
                player1.rocker_launcher = False
                player1.ak_47_rifle = False
                print(colors.green + 'Default stats have been loaded/saved and a new game will begin...\n',
                      colors.reset)
                sleep(1)
                checkpoint_save()
                game_intro_description()
            elif choice.lower() in ['c', 'continue']:
                print(colors.green + 'Continuing game...\n', colors.reset)
                sleep(1)
            else:
                error_message()
    except FileNotFoundError:
        difficulty()

    if player1.user_health <= 0:
        print(colors.red + 'You currently have no health left...\n', colors.reset)
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
        print(colors.red + 'You currently have no health left...\n', colors.reset)
        sleep(1)
        bad_ending()

    player1.merchant_luck = random.randint(1, 7)

    if player1.merchant_luck == 3:
        sounds_effects.good_luck()
        print(colors.green + 'Whoosh! The lucky merchant has appeared in-front of you...\n' + colors.reset)
        sleep(1)

        if player1.user_balance <= 0:
            print(colors.yellow + 'Uh-Oh! You do not have enough money to buy anything... keep playing to acquire more '
                                  'money!\n', colors.reset)
            sleep(1)
        else:
            user_choice = str(input('Would you like to buy from the merchant or skip past the merchant (buy / skip): '))
            print()
            sleep(1)

            if user_choice.lower() in ['b', 'buy', 'y', 'yes']:
                print(colors.green + 'Health:', player1.user_health, '\n', colors.reset)
                sleep(1)
                print(colors.green + 'Balance:', player1.user_balance, '\n', colors.reset)
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
                    print(colors.green + 'Spiked Baseball Bat has been purchased!\n', colors.reset)
                    player1.baseball_bat = True
                    sleep(1)
                elif user_item_buy == 2 and player1.user_balance >= 15:
                    sounds_effects.merchant_purchase_sound()
                    player1.user_balance -= 15
                    print(colors.green + '1997 Beretta Pistol has been purchased!\n', colors.reset)
                    player1.beretta_pistol = True
                    sleep(1)
                elif user_item_buy == 3 and player1.user_balance >= 25:
                    sounds_effects.merchant_purchase_sound()
                    print(colors.green + '1999 AK-47 Assault Rifle has been purchased!\n', colors.reset)
                    player1.user_balance -= 25
                    player1.ak_47_rifle = True
                    sleep(1)
                elif user_item_buy == 4 and player1.user_balance >= 100:
                    sounds_effects.merchant_purchase_sound()
                    print(colors.green + 'Rocket Missile Launcher has been purchased!\n', colors.reset)
                    player1.user_balance -= 100
                    player1.rocker_launcher = True
                    sleep(1)
                elif user_item_buy == 5:
                    print(colors.green + 'Purchasing from the merchant has been skipped...\n', colors.reset)
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
    if player1.rocker_launcher:
        player1.user_health -= 0
        print(colors.green + 'You have used the rocker missile launcher and defeated the zombies without losing any '
                             'health!\n', colors.reset)
        sleep(2)
    elif player1.ak_47_rifle:
        player1.user_health -= 10
        print(colors.green + 'You have used the ak-47 rifle and defeated the zombies with only losing 10 health!\n',
              colors.reset)
        sleep(2)
    elif player1.beretta_pistol:
        player1.user_health -= 25
        print(colors.green + 'You have used the beretta pistol and defeated the zombies with only losing 25 health!\n',
              colors.reset)
        sleep(2)
    elif player1.baseball_bat:
        player1.user_health -= 35
        print(colors.green + 'You have used the baseball bat and defeated the zombies with losing 35 health!\n',
              colors.reset)
        sleep(2)
    elif player1.starting_knife:
        player1.user_health -= 45
        print(colors.green + 'You have used the starting knife and defeated the zombies with losing 45 health!\n',
              colors.reset)
        sleep(2)
    else:
        player1.user_health = 0
        print(colors.red + 'Due to not having any available weapons or guns on you... You automatically cannot defend\n'
                           'yourself and you have lost all of your health!\n', colors.reset)
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
            print(
                colors.green + 'You have successfully defended off the zombies inside the gas station but it was most '
                               'unfortunate the man you found could not make it...\n', colors.reset)
            sleep(2)
            user_choice = int(input('You have the choice to either (1) Search the all the bodies of zombies and the '
                                    'dead man (2) Head over to the local Diner: '))
            print()
            sleep(1)

            if user_choice == 1:
                random_money = random.randint(5, 30)
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
        random_money = random.randint(5, 30)
        print('The man hands over some cash (' + str(random_money),
              'dollars) and tells you about a mysterious lurking salesman who would wonder around the town quite '
              'often... The man says that he has not seen him since the apocalypse has happened but keep the money on '
              'you in-case he shows...\n')
        player1.user_balance += random_money
        sleep(2.5)
        sounds_effects.wind_sound()
        print('You give thanks to the man and exit the local Gas Station and make your way down a tumbled and broken '
              'road... The gleaming fog and ashe outside is giving way to your vision and you see more and more '
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
          'a single friendly soul insight... You start to come to a conclusion about where everybody in the small '
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
            random_money = random.randint(5, 30)
            print('You attacked the zombie with the knife you found earlier and killed the zombie while losing 15 '
                  'health... You search the body of the zombie and woman to find a total of', random_money,
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
        random_money = random.randint(5, 30)
        random_health = random.randint(5, 15)
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
              'familiar face... You see the face of the man you met earlier at the local Gas Station taking a group '
              'family picture!\n')
        sleep(3)
        sounds_effects.horror_sound_effects()
        print('Since you are finished exploring and searching the diner area, you proceed on your path to the '
              'parkview area...\n')
        sleep(3.5)
        parkview_area()

    elif user_choice == 2:
        sounds_effects.zombie_attack_outside()
        print(colors.red + 'Upon leaving the diner area, you come across a group of about 5 zombies heading directly '
                           'towards you!\n', colors.reset)
        sleep(1.5)
        user_attack()

        if player1.user_health > 0:
            print(colors.green + 'You have successfully defended off the zombies outside the local Diner... You will '
                                 'now head over to the Parkview Area\n', colors.reset)
            sleep(2)
            parkview_area()

        else:
            bad_ending()

    else:
        error_message()


def broken_roads_area():
    sounds_effects.zombie_attack_outside()
    print('You have reached the broken roads area and managed to find a running vehicle but there are a group of '
          'about 3 zombies surrounding the vehicle... The zombies begin to head directly towards you and you prepare '
          'to fight once more...\n')
    sleep(4.5)
    user_attack()
    checkpoint_save()

    if player1.user_health > 0:
        sounds_effects.horror_sound_effects()
        print(colors.green + 'You have successfully fought off the zombies surrounding the running vehicle... You then '
                             'enter the running vehicle... The manage to put the vehicle into drive and you drive '
                             'away into the sunrise...\n')
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
                random_money = random.randint(5, 30)
                print(colors.green + 'You have successfully killed the man! Upon searching his body, you find a total '
                                     'of', random_money, 'dollars!\n', colors.reset)
                player1.user_balance += random_money
                sleep(1)
                checkpoint_save()
                sounds_effects.horror_sound_effects()
                print('You now decide to leave the parkview area...\n')
                sleep(1.5)
                broken_roads_area()

            else:
                sounds_effects.bad_luck()
                print(colors.red + 'The man has killed you and zombies start to feast on your dead decaying flesh...'
                                   '\n', colors.reset)
                sleep(2)
                bad_ending()

        elif user_choice == 2:
            sounds_effects.bad_luck()
            user_attack()

            if player1.user_health > 0:
                random_money = random.randint(5, 30)
                print(colors.green + 'You have successfully killed the man! Upon searching his body, you find a total '
                                     'of', random_money, 'dollars!\n', colors.reset)
                player1.user_balance += random_money
                sleep(1)
                checkpoint_save()
                sounds_effects.horror_sound_effects()
                print('You now decide to leave the Parkview Area...\n')
                sleep(1.5)
                broken_roads_area()

            else:
                sounds_effects.bad_luck()
                print(colors.red + 'The man has killed you and zombies start to feast on your dead decaying flesh...'
                                   '\n', colors.reset)
                sleep(2)
                bad_ending()

    elif user_choice == 2:
        broken_roads_area()
    else:
        error_message()


def difficulty():
    print(colors.green + '(1) Easy\n' + colors.reset + colors.yellow + '(2) Medium\n' + colors.reset + colors.red +
          '(3) Hardcore\n' + colors.reset)
    player1.user_difficulty = int(input('Select a difficulty: '))
    print()
    sleep(1)
    sounds_effects.difficulty_select_sound()

    if player1.user_difficulty == 1:
        print(colors.green + 'Easy mode has been selected, you will begin with 200 health.\n' + colors.reset)
        player1.user_health = 200
        sleep(1)
    elif player1.user_difficulty == 2:
        print(colors.yellow + 'Medium mode has been selected, you will begin with 100 health.\n' + colors.reset)
        player1.user_health = 100
        sleep(1)
    elif player1.user_difficulty == 3:
        print(colors.red + 'Hardcore mode has been selected, you will begin with only 50 health.\n' + colors.reset)
        player1.user_health = 50
        sleep(1)
    else:
        error_message()


def restart():
    restart_choice = str(input('Would you like to restart the game (yes / no): '))
    print()

    if restart_choice.lower() in ['y', 'yes']:
        if player1.user_difficulty == 1:
            print(colors.green + 'You will begin with 200 health.\n' + colors.reset)
            player1.user_health = 200
        elif player1.user_difficulty == 2:
            print(colors.green + 'You will begin with 100 health.\n' + colors.reset)
            player1.user_health = 100
        elif player1.user_difficulty == 3:
            print(colors.green + 'You will begin with 50 health.\n' + colors.reset)
            player1.user_health = 50
        else:
            print(colors.yellow + 'Since a saved difficulty value could not be found... you will start with 100 '
                                  'health...\n', colors.reset)
            sleep(1)
            player1.user_health = 100
        player1.user_balance = 0
        player1.merchant_luck = 0
        player1.baseball_bat = False
        player1.beretta_pistol = False
        player1.starting_knife = False
        player1.rocker_launcher = False
        player1.ak_47_rifle = False
        print(colors.green + 'Default stats have been loaded/saved and a new game will begin...\n', colors.reset)
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
    print(colors.green + 'Congratulations, you have survived and reached the end of the horrors...\n', colors.reset)
    sleep(1)
    print(colors.green + 'You survived with a total of', player1.user_health, 'health left!\n', colors.reset)
    sleep(1)
    checkpoint_save()
    restart()


def bad_ending():
    sounds_effects.bad_ending()
    print(colors.red + 'You have died and not reached the end of the horrors...\n', colors.reset)
    sleep(1)
    checkpoint_save()
    restart()


def error_message():
    sleep(1)
    sounds_effects.bad_luck()
    print(colors.red + 'An error has been found... restarting game...\n', colors.reset)
    sleep(2)
    game()


def checkpoint_save():
    if player1.user_health <= 0:
        print(colors.red + 'You have reached a checkpoint and currently have no more health! You have lost the game!\n',
              colors.reset)
        sleep(1)
        restart()
    merchant()
    print(colors.green + 'A checkpoint has been reached...\n', colors.reset)
    sleep(.5)
    game_data.save_game(player1)  # Sends player1 info to save file
    print(colors.green + 'Current Health:', player1.user_health, '\n')
    sleep(1)
    print(colors.green + 'Current Balance:', player1.user_balance, '\n')
    sleep(1)
    print(colors.green + 'Current Difficulty:', player1.user_difficulty, '\n', colors.reset)
    sleep(1)


if __name__ == '__main__':
    load_or_save_data()
    game_intro_description()

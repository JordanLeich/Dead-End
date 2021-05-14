#!/usr/bin/python3

# Made by Jordan Leich & Mordy Waldner on 5/11/2021, Last updated on 5/14/2021, Version 2.0


# Imports
import colors
import json
import time
import random

import sounds_effects

try:
    with open('data.json', 'r') as data:
        print(colors.green + 'Saved data checkpoint has been found!', colors.reset)
        data = json.load(data)
        user_balance = data['Balance']
        user_health = data['Health']
        merchant_luck = data['Merchant Luck']
        starting_knife = data['Starting Knife']
        baseball_bat = data['Baseball Bat']
        beretta_pistol = data['Beretta Pistol']
        ak_47_rifle = data['AK 47 Rifle']
        rocker_launcher = data['Rocket Missile Launcher']
        print(colors.green + 'Saved data has been loaded successfully!\n', colors.reset)
except FileNotFoundError:
    print()
    print(colors.yellow + 'No saved data found...\n' + colors.reset + colors.green + 'Starting a fresh game...\n' +
          colors.reset)
    user_balance = 0
    user_health = 0
    merchant_luck = 0
    baseball_bat = False
    beretta_pistol = False
    starting_knife = False
    rocker_launcher = False
    ak_47_rifle = False
    time.sleep(1)


def game_intro_description():
    sounds_effects.intro_sound()
    print('This is a zombie survival game where you must make the best choices and decisions possible in order to live.'
          ' As a survivor, you will encounter zombies, weapons, people, and a merchant to buy from with an '
          'in-game currency. Every decision you make has a cause and effect while some lead you to fortune and others '
          'lead you to death.\n')
    time.sleep(2.5)
    game()


def game():
    global user_health, user_balance, merchant_luck, starting_knife, ak_47_rifle, beretta_pistol, baseball_bat, \
        rocker_launcher
    difficulty()

    print('You have ended up in a small local town called Hinesville. This old town contains a population of about '
          'only 6000 people and holds only a gas station, local diner, and a park. The current year is 1999 and you '
          'cannot wait to finally get on with your life and move somewhere more alive\n')
    time.sleep(2)
    user_choice1 = int(input('While sitting down in your living room apartment, you can either (1) look around or '
                             '(2) walk outside: '))
    print()
    time.sleep(1)

    if user_choice1 == 1:
        print('You have decided to look around your apartment and decide to grab a concealed knife that you legally '
              'are allowed to carry in public areas just in case anything happens...\n')
        time.sleep(1)
        starting_knife = True
        outside_area()
    elif user_choice1 == 2:
        time.sleep(1)
        starting_knife = False
        outside_area()
    else:
        error_message()


def merchant():
    global merchant_luck, user_balance, baseball_bat, beretta_pistol, ak_47_rifle, rocker_launcher
    merchant_luck = random.randint(1, 7)

    if merchant_luck == 4:
        # Add a good luck sound effect here
        print(colors.green + 'Whoosh! The lucky merchant has appeared in-front of you...\n' + colors.reset)
        time.sleep(1)

        if user_balance <= 0:
            print(colors.yellow + 'Uh-Oh! You do not have enough money to buy anything... keep playing to acquire more '
                                  'money!\n', colors.reset)
            time.sleep(1)

        user_choice = str(input('Would you like to buy from the merchant or skip past the merchant (buy / skip): '))
        print()
        time.sleep(1)

        if user_choice.lower() == 'b' or user_choice.lower() == 'buy' or user_choice.lower() == 'y' or user_choice. \
                lower() == 'yes':
            user_item_buy = int(input('''--- Merchants inventory ---
(1) Spiked Baseball Bat (5 Dollars)
(2) 1997 Beretta Pistol (15 Dollars)
(3) 1999 AK-47 Assault Rifle (25 Dollars)
(4) Rocket Missile Launcher (100 Dollars)
What would you like to buy or skip the merchant: '''))
            print()
            time.sleep(1)

            if user_item_buy == 1:
                user_balance -= 5
                print(colors.green + 'Spiked Baseball Bat has been purchased!\n', colors.reset)
                baseball_bat = True
                time.sleep(1)
            elif user_item_buy == 2:
                user_balance -= 15
                print(colors.green + '1997 Beretta Pistol has been purchased!\n', colors.reset)
                beretta_pistol = True
                time.sleep(1)
            elif user_item_buy == 3:
                print(colors.green + '1999 AK-47 Assault Rifle has been purchased!\n', colors.reset)
                user_balance -= 25
                ak_47_rifle = True
                time.sleep(1)
            elif user_item_buy == 4:
                print(colors.green + 'Rocket Missile Launcher has been purchased!\n', colors.reset)
                user_balance -= 100
                rocker_launcher = True
                time.sleep(1)
            else:
                error_message()

        elif user_choice.lower() == 's' or user_choice.lower() == 'sell' or user_choice.lower() == 'n' or user_choice. \
                lower() == 'no':
            print('The merchant has been skipped but can be brought back later...\n')
            time.sleep(1)
        else:
            error_message()


def continue_message():
    print('continue story here')
    quit()


def gas_station():
    global user_health, user_balance, merchant_luck, starting_knife, rocker_launcher, baseball_bat, beretta_pistol, \
        ak_47_rifle
    sounds_effects.horror_sound_effects()
    print('You have entered the local gas station...\n\n' + colors.green + 'A checkpoint has been reached...\n',
          colors.reset)
    time.sleep(1)

    merchant()

    with open('data.json', 'w') as user_data_file:
        user_data_file.write(json.dumps({'Balance': user_balance, 'Health': user_health,
                                         'Merchant Luck': merchant_luck, 'Starting Knife': starting_knife,
                                         'Baseball Bat': baseball_bat, 'Beretta Pistol': beretta_pistol,
                                         'AK 47 Rifle': ak_47_rifle, 'Rocket Missile Launcher': rocker_launcher}))

    continue_message()


def outside_area():
    global user_health, user_balance, merchant_luck, starting_knife
    print('You make your way to the outside area...\n')
    time.sleep(1)
    print('You instantly notice something is not right... a dark gloomy fog covers all of the town and you do not see '
          'a single friendly soul insight... You start to come to a conclusion about where everybody in the small '
          'town of Hinesville has went but nothing is making sense...\n')
    time.sleep(2)
    user_choice = int(input('You have the choice to either explore (1) outside area or (2) visit the local gas '
                            'station: '))
    print()
    time.sleep(1)

    if user_choice == 1:
        print('You decide to explore the outside area and along the way, you see a woman bleeding out on the ground '
              'with the shape of a man figure hovering over her...\n')
        time.sleep(2)
        sounds_effects.zombie_attack_outside()
        print('Lone behold... the figure is eating the woman alive but you are too late to rescue her!\n')
        time.sleep(1.5)
        user_choice = int(input('Since you have the knife on you already, (1) do you attack the zombie or (2) '
                                'avoid the zombie and run to the local gas station: '))
        print()
        time.sleep(1)

        if user_choice == 1:
            sounds_effects.zombie_attack_outside()
            print('You attacked the zombie with the knife you found earlier and killed the zombie... '
                  'You search the body of the zombie and woman and find a total of 11 Dollars...\n')
            time.sleep(2)
            continue_message()

        elif user_choice == 2:
            gas_station()
        else:
            error_message()

    elif user_choice == 2:
        gas_station()
    else:
        error_message()


def difficulty():
    global user_health
    print(colors.green + 'Easy\n' + colors.reset + colors.yellow + 'Medium\n' + colors.reset + colors.red + 'Hardcore\n'
          + colors.reset)

    user_difficulty = str(input('Select a difficulty: '))
    print()
    time.sleep(1)
    sounds_effects.difficulty_select_sound()

    if user_difficulty.lower() == 'e' or user_difficulty.lower() == 'easy':
        print(colors.green + 'Easy mode has been selected, you will begin with 200 health.\n' + colors.reset)
        user_health = 200
        time.sleep(1)
    elif user_difficulty.lower() == 'm' or user_difficulty.lower() == 'medium':
        print(colors.yellow + 'Medium mode has been selected, you will begin with 100 health.\n' + colors.reset)
        user_health = 100
        time.sleep(1)
    elif user_difficulty.lower() == 'h' or user_difficulty.lower() == 'hard':
        print(colors.red + 'Hardcore mode has been selected, you will begin with only 50 health.\n' + colors.reset)
        user_health = 50
        time.sleep(1)
    else:
        error_message()


def restart():
    restart_choice = str(input('Would you like to restart the game (yes / no): '))

    if restart_choice.lower() == 'y' or restart_choice.lower() == 'yes':
        game_intro_description()
    elif restart_choice.lower() == 'n' or restart_choice.lower() == 'no':
        print('Ending game...')
        time.sleep(.5)
        quit()
    else:
        error_message()


def end_game():
    print(colors.green + 'Congratulations, you have reached the end of the horrors...\n', colors.reset)
    time.sleep(1.5)
    restart()


def error_message():
    time.sleep(1)
    # add a bad luck sound effect here
    print(colors.red + 'An error has been found... restarting game...\n', colors.reset)
    time.sleep(2)
    game()


game_intro_description()

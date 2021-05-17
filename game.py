#!/usr/bin/python3

# Made by Jordan Leich & Mordy Waldner on 5/11/2021, Last updated on 5/17/2021, Version 2.6


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
        rocker_launcher, data

    try:
        with open('data.json', 'r') as data:
            sounds_effects.difficulty_select_sound()
            print(colors.green + 'Difficulty screen skipped due to saved data already existing...\n', colors.reset)
            time.sleep(1)
    except FileNotFoundError:
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
        outside_area()
    else:
        error_message()


def merchant():
    global merchant_luck, user_balance, baseball_bat, beretta_pistol, ak_47_rifle, rocker_launcher
    merchant_luck = random.randint(1, 7)

    if merchant_luck == 4:
        sounds_effects.good_luck()
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
            print(colors.green + 'Your current cash balance is:', user_balance, '\n', colors.reset)
            time.sleep(1)
            user_item_buy = int(input('''--- Merchants inventory ---
(1) Spiked Baseball Bat (5 Dollars)
(2) 1997 Beretta Pistol (15 Dollars)
(3) 1999 AK-47 Assault Rifle (25 Dollars)
(4) Rocket Missile Launcher (100 Dollars)
What would you like to buy or skip the merchant: '''))
            print()
            time.sleep(1)

            if user_item_buy == 1 and user_balance >= 5:
                sounds_effects.merchant_purchase_sound()
                user_balance -= 5
                print(colors.green + 'Spiked Baseball Bat has been purchased!\n', colors.reset)
                baseball_bat = True
                time.sleep(1)
            elif user_item_buy == 2 and user_balance >= 15:
                sounds_effects.merchant_purchase_sound()
                user_balance -= 15
                print(colors.green + '1997 Beretta Pistol has been purchased!\n', colors.reset)
                beretta_pistol = True
                time.sleep(1)
            elif user_item_buy == 3 and user_balance >= 25:
                sounds_effects.merchant_purchase_sound()
                print(colors.green + '1999 AK-47 Assault Rifle has been purchased!\n', colors.reset)
                user_balance -= 25
                ak_47_rifle = True
                time.sleep(1)
            elif user_item_buy == 4 and user_balance >= 100:
                sounds_effects.merchant_purchase_sound()
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


def user_attack():
    if rocker_launcher:
        user_health -= 0
        print('You have used the rocker missile launcher and defeated the zombies without losing any health!\n')
        time.sleep(1)
    elif ak_47_rifle:
        user_health -= 10
        print('You have used the ak-47 rifle and defeated the zombies with only losing 10 health!\n')
        time.sleep(1)
    elif beretta_pistol:
        user_health -= 25
        print('You have used the beretta pistol and defeated the zombies with only losing 25 health!\n')
        time.sleep(1)
    elif baseball_bat:
        user_health -= 35
        print('You have used the baseball bat and defeated the zombies with losing 35 health!\n')
        time.sleep(1)
    elif starting_knife:
        user_health -= 45
        print('You have used the starting knife and defeated the zombies with losing 45 health!\n')
        time.sleep(1)
    elif not starting_knife and not baseball_bat and not beretta_pistol and not ak_47_rifle and not rocker_launcher:
        print(colors.red + 'Due to not having any available weapons or guns on you... You automatically cannot defend '
                           'yourself and you have lost all of your health!\n', colors.reset)
        time.sleep(2)
        good_ending()
    else:
        error_message()


def gas_station():
    global user_health, user_balance, merchant_luck, starting_knife, rocker_launcher, baseball_bat, beretta_pistol, \
        ak_47_rifle
    sounds_effects.horror_sound_effects()
    print('You have entered the local gas station...\n\n' + colors.green + 'A checkpoint has been reached...\n',
          colors.reset)
    time.sleep(1)

    checkpoint_save()

    print('From the front counter, you see a man who points his gun at you while you walk in! The man tells you to '
          'freeze but then notices that you are a survivor just like him... You both discuss and try to figure out '
          'what the hell is going on in this city and the man tells you that there has been a bacteria that can '
          'contaminated all meat supply chains across the world...\n')
    time.sleep(5)
    user_choice = int(input('You have the choice to either (1) keep talking to the man or (2) ask the man for any '
                            'supplies along your journey: '))
    print()
    time.sleep(1)

    if user_choice == 1:
        print('As you keep talking to the man, he starts to tell you about his family and how they would always '
              'venture out to the park with his young daughter and son...\n')
        time.sleep(2)
        sounds_effects.zombie_attack_inside()
        print('Out of nowhere, a group of 3 zombies begin to bang on the glass door from which you entered in from...'
              '\n')
        time.sleep(2.5)
        sounds_effects.zombie_attack_inside()
        print('While attempting to save you, the man fights off 2 zombies with his pump shotgun and get eaten alive '
              'while saying, RUN! but more zombies come to arise on you...\n')
        time.sleep(2.5)
        print('You decide to fight off the zombies in the will of your hopes for living...\n')
        time.sleep(1.5)

        user_attack()

        continue_message()

    elif user_choice == 2:
        print('The man hands over some cash (16 dollars) and tells you about a mysterious lurking salesman who would '
              'wonder around the town quite often... The man says that he has not seen him since the apocalypse has '
              'happened but keep the money on you in-case he shows...\n')
        user_balance += 16
        time.sleep(2)
        print('You give thanks to the man and exit the local gas station and make your way down a tumbled and broken '
              'road... The gleaming fog and ashe outside is giving way to your vision and you see more and more '
              'unclear... Deep down inside... you know you must go on further...\n')
        time.sleep(2)
        checkpoint_save()
        continue_message()
    else:
        error_message()


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
        user_choice = int(input('(1) attack the zombie or (2) avoid the zombie and run to the local gas station: '))
        print()
        time.sleep(1)

        if user_choice == 1:
            sounds_effects.zombie_attack_outside()
            print('You attacked the zombie with the knife you found earlier and killed the zombie while losing 15 '
                  'health... You search the body of the zombie and woman and find a total of 11 Dollars...\n')
            user_balance += 11
            user_health -= 15
            time.sleep(2)
            print('You then finally get to make your way over to the local gas station...\n')
            time.sleep(1)
            gas_station()

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


def good_ending():
    print(colors.green + 'Congratulations, you have reached the end of the horrors...\n', colors.reset)
    time.sleep(1.5)
    checkpoint_save()
    restart()


def bad_ending():
    print(colors.red + 'You have not reached the end of the horrors...\n', colors.reset)
    time.sleep(1.5)
    checkpoint_save()
    restart()


def error_message():
    time.sleep(1)
    sounds_effects.bad_luck()
    print(colors.red + 'An error has been found... restarting game...\n', colors.reset)
    time.sleep(2)
    game()


def checkpoint_save():
    merchant()
    with open('data.json', 'w') as user_data_file:
        user_data_file.write(json.dumps({'Balance': user_balance, 'Health': user_health,
                                         'Merchant Luck': merchant_luck, 'Starting Knife': starting_knife,
                                         'Baseball Bat': baseball_bat, 'Beretta Pistol': beretta_pistol,
                                         'AK 47 Rifle': ak_47_rifle, 'Rocket Missile Launcher': rocker_launcher}))


game_intro_description()

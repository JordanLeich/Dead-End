#!/usr/bin/python3

# Made by Jordan Leich on 5/11/2021, Last updated on 5/13/2021, Version 1.2

# TODO List add a merchant, add a save feature, complete the storyline

# Imports
import colors
import json
import time
import random

# Global variables
user_balance = 0
user_health = 0

try:
    with open('data.json', 'r') as data:
        data = json.load(data)
        print(data)
except FileNotFoundError:
    print(f'{colors.green}No saved data found...\nStarting fresh game\n{colors.reset}')

def game_intro_description():
    print('start here, this game is about...\n')
    game()


def game():
    global user_health, user_balance
    user_name = str(input('What is your survivors name? '))
    print()
    difficulty()

    print('You have ended up in a small local town called Hinesville. This old town contains a population of about '
          'only 6000 people and holds only a gas station, local diner, and a park. The current year is 1999 and you '
          'cannot wait to finally get on with your life and move somewhere more alive\n')
    user_choice1 = int(input('While sitting down in your living room apartment, you can either (1) look around or '
                             '(2) walk outside: '))

    if user_choice1 == 1:
        print('You have decided to look around your apartment and decide to grab a concealed knife that you legally '
              'are allowed to carry in public areas just in case something happens...\n')
        starting_knife = True
        outside_area()
    elif user_choice1 == 2:
        starting_knife = False
        outside_area()
    else:
        error_message()


def gas_station():
    print('You have entered the local gas station...\n')


def outside_area():
    global user_health, user_balance
    print('You make your way to the outside area...\n')
    print('You instantly notice something is not right... a dark gloomy fog covers all of the town and you do not see '
          'a single friendly soul insight... You start to come to a conclusion about where everybody in the small '
          'town of Hinesville has went but nothing is making sense...\n')
    user_choice2 = int(input('You have the choice to either explore (1) outside area or (2) '
                             'visit the local gas station: '))
    print()

    if user_choice2 == 1:
        print()
    elif user_choice2 == 2:
        gas_station()
    else:
        error_message()


def difficulty():
    print(colors.green + 'Easy\n' + colors.reset + colors.yellow + 'Medium\n' + colors.reset + colors.red + 'Hardcore\n'
          + colors.reset)

    user_difficulty = str(input('Select a difficulty: '))
    print()

    if user_difficulty.lower() == 'e' or user_difficulty.lower() == 'easy':
        print(colors.green + 'Easy mode has been selected, you will begin with 200 health.\n' + colors.reset)
        user_health = 200
    elif user_difficulty.lower() == 'm' or user_difficulty.lower() == 'medium':
        print(colors.yellow + 'Medium mode has been selected, you will begin with 100 health.\n' + colors.reset)
        user_health = 100
    elif user_difficulty.lower() == 'h' or user_difficulty.lower() == 'hard':
        print(colors.red + 'Hardcore mode has been selected, you will begin with only 50 health.\n' + colors.reset)
        user_health = 50
    else:
        error_message()


def error_message():
    print(colors.red + 'An error has been found... restarting game...\n' + colors.reset)
    time.sleep(2)
    game()


game_intro_description()

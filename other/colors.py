# Created by Jordan Leich on 7/27/2020

from colored import fg, attr

GREEN = fg('green')
RED = fg('red')
YELLOW = fg('yellow')
BLUE = fg('blue')
RESET = attr('reset')

def print_green(message_text):
    print(f'{GREEN}{message_text}{RESET}')

def print_red(message_text):
    print(f'{RED}{message_text}{RESET}')

def print_yellow(message_text):
    print(f'{YELLOW}{message_text}{RESET}')

def print_blue(message_text):
    print(f'{BLUE}{message_text}{RESET}')

def user_error(message_text):
    print_red(message_text)

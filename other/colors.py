""" File is called when colored text is printed to the screen. """
# Created by Jordan Leich on 7/27/2020

from colored import fg, attr
from time import sleep


GREEN = fg('green')
RED = fg('red')
YELLOW = fg('yellow')
BLUE = fg('blue')
RESET = attr('reset')


def print_green(message_text, sleep_duration=0):
    """prints text in green with a sleep duration and resets the color back to default"""
    print(f'{GREEN}{message_text}{RESET}')
    sleep(sleep_duration)


def print_red(message_text, sleep_duration=0):
    """prints text in red with a sleep duration and resets the color back to default"""
    print(f'{RED}{message_text}{RESET}')
    sleep(sleep_duration)


def print_yellow(message_text, sleep_duration=0):
    """prints text in yellow with a sleep duration and resets the color back to default"""
    print(f'{YELLOW}{message_text}{RESET}')
    sleep(sleep_duration)


def print_blue(message_text, sleep_duration=0):
    """prints text in blue with a sleep duration and resets the color back to default"""
    print(f'{BLUE}{message_text}{RESET}')
    sleep(sleep_duration)


def user_error(message_text, sleep_duration=0):
    """prints error text message a sleep duration"""
    print_red(message_text, sleep_duration)


# print and sleep
def print_sleep(message_text, sleep_duration=0):
    """prints text with a sleep duration"""
    print(message_text)
    sleep(sleep_duration)

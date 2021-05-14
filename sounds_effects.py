import random
import time
from pygame import *
import pygame

import colors


def intro_sound():
    mixer.init()
    mixer.music.load('sounds/introsoundtrack.mp3')
    mixer.music.play()


def difficulty_select_sound():
    soundObj = pygame.mixer.Sound('sounds/deep_doom.wav')
    soundObj.play()


def horror_sound_effects():
    number = random.randint(1, 3)

    if number == 1:
        mixer.init()
        mixer.music.load('sounds/horrorsoundeffect1.mp3')
        mixer.music.play()
    elif number == 2:
        mixer.init()
        mixer.music.load('sounds/horrorsoundeffect2.mp3')
        mixer.music.play()
    elif number == 3:
        mixer.init()
        mixer.music.load('sounds/horrorsoundeffect3.mp3')
        mixer.music.play()
    else:
        error_message()


def zombie_attack_inside():
    number = random.randint(1, 3)

    if number == 1:
        mixer.init()
        mixer.music.load('sounds/zombieattack1inside.mp3')
        mixer.music.play()
    elif number == 2:
        mixer.init()
        mixer.music.load('sounds/zombieattack2inside.mp3')
        mixer.music.play()
    elif number == 3:
        mixer.init()
        mixer.music.load('sounds/zombieattack3inside.mp3')
        mixer.music.play()
    else:
        error_message()


def zombie_attack_outside():
    number = random.randint(1, 3)

    if number == 1:
        mixer.init()
        mixer.music.load('sounds/zombieattack1outside.mp3')
        mixer.music.play()
    elif number == 2:
        mixer.init()
        mixer.music.load('sounds/zombieattack2outside.mp3')
        mixer.music.play()
    elif number == 3:
        mixer.init()
        mixer.music.load('sounds/zombieattack3outside.mp3')
        mixer.music.play()
    else:
        error_message()


def error_message():
    print(colors.red + 'Sound effect error found...\n', colors.reset)
    time.sleep(2)
    quit()

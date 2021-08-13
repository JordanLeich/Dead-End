import random
import time
from pygame import *
import pygame
from other import colors


def intro_sound():
    mixer.init()
    mixer.music.load('sounds/introsoundtrack.mp3')
    mixer.music.play()


def bad_ending():
    soundObj = pygame.mixer.Sound('sounds/dark_element_burst.wav')
    soundObj.play()


def difficulty_select_sound():
    soundObj = pygame.mixer.Sound('sounds/deep_doom.wav')
    soundObj.play()


def bad_luck():
    number = random.randint(1, 3)

    if number == 1:
        soundObj = pygame.mixer.Sound('sounds/badluck.wav')
        soundObj.play()
    elif number == 2:
        soundObj = pygame.mixer.Sound('sounds/dark_slam.wav')
        soundObj.play()
    elif number == 3:
        soundObj = pygame.mixer.Sound('sounds/effect_horror_alerted.wav')
        soundObj.play()
    else:
        error_message()


def good_luck():
    soundObj = pygame.mixer.Sound('sounds/goodluck.wav')
    soundObj.play()


def merchant_purchase_sound():
    number = random.randint(1, 2)

    if number == 1:
        soundObj = pygame.mixer.Sound('sounds/cashreg.wav')
        soundObj.play()
    elif number == 2:
        soundObj = pygame.mixer.Sound('sounds/metal_shing.wav')
        soundObj.play()


def horror_sound_effects():
    number = random.randint(1, 7)

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
    elif number == 4:
        soundObj = pygame.mixer.Sound('sounds/ghost_movement.wav')
        soundObj.play()
    elif number == 5:
        soundObj = pygame.mixer.Sound('sounds/supernatural.wav')
        soundObj.play()
    elif number == 6:
        soundObj = pygame.mixer.Sound('sounds/spooky_breathe_evil.wav')
        soundObj.play()
    elif number == 7:
        soundObj = pygame.mixer.Sound('sounds/spooky_ambience.wav')
        soundObj.play()
    else:
        error_message()


def wind_sound():
    soundObj = pygame.mixer.Sound('sounds/heavy_wind.wav')
    soundObj.play()


def zombie_attack_inside():
    number = random.randint(1, 5)

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
    elif number == 4:
        soundObj = pygame.mixer.Sound('sounds/monster_screech.wav')
        soundObj.play()
    elif number == 5:
        soundObj = pygame.mixer.Sound('sounds/breathe_ghost_eerie.wav')
        soundObj.play()
    else:
        error_message()


def parkview_entrance():
    soundObj = pygame.mixer.Sound('sounds/spooky_werewolf_howl.wav')
    soundObj.play()


def climatic():
    number = random.randint(1, 2)

    if number == 1:
        soundObj = pygame.mixer.Sound('sounds/climatic.wav')
        soundObj.play()
    elif number == 2:
        soundObj = pygame.mixer.Sound('sounds/action_riser.wav')
        soundObj.play()
    else:
        error_message()


def zombie_attack_outside():
    number = random.randint(1, 5)

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
    elif number == 4:
        soundObj = pygame.mixer.Sound('sounds/monster_ghost_death.wav')
        soundObj.play()
    elif number == 5:
        soundObj = pygame.mixer.Sound('sounds/breathe_ghost_eerie.wav')
        soundObj.play()
    else:
        error_message()


def error_message():
    print(colors.red + 'Sound effect error found...\n', colors.reset)
    time.sleep(2)
    quit()

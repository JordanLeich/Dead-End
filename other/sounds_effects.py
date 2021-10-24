from random import randint
import pygame

# plays all the sounds given from file path
def _play_sound(file_path):
    pygame.mixer.init()
    soundObj = pygame.mixer.Sound(file_path)
    soundObj.play()


def intro_sound():
    _play_sound('sounds/introsoundtrack.mp3')


def bad_ending():
    _play_sound('sounds/dark_element_burst.wav')


def difficulty_select_sound():
    _play_sound('sounds/deep_doom.wav')


def bad_luck():
    badluck_paths = ['sounds/badluck.wav', 
                     'sounds/dark_slam.wav',
                     'sounds/effect_horror_alerted.wav',
                    ]
    _play_sound(badluck_paths[randint(0, len(badluck_paths)-1)])

def good_luck():
    _play_sound('sounds/goodluck.wav')


def merchant_purchase_sound():
    merchant_paths = ['sounds/cashreg.wav', 
                      'sounds/metal_shing.wav',
                     ]
    _play_sound(merchant_paths[randint(0, len(merchant_paths)-1)])


def horror_sound_effects():
    horror_paths = ['sounds/horrorsoundeffect1.mp3',
                    'sounds/horrorsoundeffect2.mp3',
                    'sounds/horrorsoundeffect3.mp3',
                    'sounds/ghost_movement.wav',
                    'sounds/supernatural.wav',
                    'sounds/spooky_breathe_evil.wav',
                    'sounds/spooky_ambience.wav',
                   ]
    _play_sound(horror_paths[randint(0, len(horror_paths)-1)])


def wind_sound():
    _play_sound('sounds/heavy_wind.wav')


def zombie_attack_inside():
    zombie_inside_path = ['sounds/zombieattack1inside.mp3',
                          'sounds/zombieattack2inside.mp3',
                          'sounds/zombieattack3inside.mp3',
                          'sounds/monster_screech.wav',
                          'sounds/breathe_ghost_eerie.wav',
                         ]
    _play_sound(zombie_inside_path[randint(0, len(zombie_inside_path)-1)])


def parkview_entrance():
    _play_sound('sounds/spooky_werewolf_howl.wav')


def climatic():
    climatic_paths = ['sounds/climatic.wav',
                      'sounds/action_riser.wav',
                     ]
    _play_sound(climatic_paths[randint(0, len(climatic_paths)-1)])


def zombie_attack_outside():
    zombie_outside_path = ['sounds/zombieattack1inside.mp3',
                           'sounds/zombieattack2inside.mp3',
                           'sounds/zombieattack3inside.mp3',
                           'sounds/monster_ghost_death.wav',
                           'sounds/breathe_ghost_eerie.wav',
                          ]
    _play_sound(zombie_outside_path[randint(0, len(zombie_outside_path)-1)])

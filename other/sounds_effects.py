from random import choice
import pygame


class Game_Sounds:
    def __init__(self):
        self.volume_level = 0.05

    def _play_sound(self, file_path):
        """
        Plays all the sounds given from file path
          """
        pygame.mixer.init()
        soundObj = pygame.mixer.Sound(file_path)
        soundObj.set_volume(self.volume_level)  # Default volume is 0.05. Max volume is 1.0 and Min volume is 0.0
        soundObj.play()

    def intro_sound(self):
        self._play_sound('sounds/introsoundtrack.mp3')

    def bad_ending(self):
        self._play_sound('sounds/dark_element_burst.wav')

    def difficulty_select_sound(self):
        self._play_sound('sounds/deep_doom.wav')

    def bad_luck(self):
        badluck_paths = ['sounds/badluck.wav',
                         'sounds/dark_slam.wav',
                         'sounds/effect_horror_alerted.wav',
                         ]
        self._play_sound(choice(badluck_paths))

    def good_luck(self):
        self._play_sound('sounds/goodluck.wav')

    def merchant_purchase_sound(self):
        merchant_paths = ['sounds/cashreg.wav',
                          'sounds/metal_shing.wav',
                          ]
        self._play_sound(choice(merchant_paths))

    def horror_sound_effects(self):
        horror_paths = ['sounds/horrorsoundeffect1.mp3',
                        'sounds/horrorsoundeffect2.mp3',
                        'sounds/horrorsoundeffect3.mp3',
                        'sounds/ghost_movement.wav',
                        'sounds/supernatural.wav',
                        'sounds/spooky_breathe_evil.wav',
                        'sounds/spooky_ambience.wav',
                        ]
        self._play_sound(choice(horror_paths))

    def wind_sound(self):
        self._play_sound('sounds/heavy_wind.wav')

    def zombie_attack_inside(self):
        zombie_inside_path = ['sounds/zombieattack1inside.mp3',
                              'sounds/zombieattack2inside.mp3',
                              'sounds/zombieattack3inside.mp3',
                              'sounds/monster_screech.wav',
                              'sounds/breathe_ghost_eerie.wav',
                              ]
        self._play_sound(choice(zombie_inside_path))

    def parkview_entrance(self):
        self._play_sound('sounds/spooky_werewolf_howl.wav')

    def climatic(self):
        climatic_paths = ['sounds/climatic.wav',
                          'sounds/action_riser.wav',
                          ]
        self._play_sound(choice(climatic_paths))

    def zombie_attack_outside(self):
        zombie_outside_path = ['sounds/zombieattack1inside.mp3',
                               'sounds/zombieattack2inside.mp3',
                               'sounds/zombieattack3inside.mp3',
                               'sounds/monster_ghost_death.wav',
                               'sounds/breathe_ghost_eerie.wav',
                               ]
        self._play_sound(choice(zombie_outside_path))

    def set_volume(self, level):
        self.volume_level = level

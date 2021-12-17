from random import choice
import pygame


class GameSounds:
    """stores the default volume level and file paths to all sounds found in the sounds folder"""

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

    def intro_sounds(self):
        """plays intro sound"""
        intro_sound_paths = ['sounds/introsoundtrack1.mp3',
                             'sounds/introsoundtrack2.mp3',
                             'sounds/introsoundtrack3.mp3',
                             'sounds/introsoundtrack4.mp3',
                             'sounds/introsoundtrack5.mp3',
                             ]
        self._play_sound(choice(intro_sound_paths))

    def bad_ending(self):
        """plays bad ending sound"""
        self._play_sound('sounds/dark_element_burst.wav')

    def difficulty_select_sound(self):
        """plays difficulty selection sound"""
        self._play_sound('sounds/deep_doom.wav')

    def bad_luck(self):
        """plays when something bad happens"""
        badluck_paths = ['sounds/badluck.wav',
                         'sounds/dark_slam.wav',
                         'sounds/effect_horror_alerted.wav',
                         ]
        self._play_sound(choice(badluck_paths))

    def good_luck(self):
        """plays when something good happens"""
        goodluck_paths = ['sounds/goodluck0.wav',
                          'sounds/goodluck1.mp3',
                          'sounds/goodluck2.wav',
                          'sounds/goodluck3.wav',
                          'sounds/goodluck4.mp3',
                          'sounds/goodluck5.mp3',
                          'sounds/goodluck6.mp3',
                          'sounds/goodluck7.mp3',
                          ]
        self._play_sound(choice(goodluck_paths))

    def merchant_purchase_sound(self):
        """plays when player buys something"""
        merchant_paths = ['sounds/cashreg.wav',
                          'sounds/metal_shing.wav',
                          ]
        self._play_sound(choice(merchant_paths))

    def horror_sound_effects(self):
        """plays when something scary happens"""
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
        """plays usually when outside"""
        wind_paths = ['sounds/heavy_wind.wav',
                      'sounds/heavy_wind2.mp3',
                      ]
        self._play_sound(choice(wind_paths))

    def menu_button_sound(self):
        """plays when the player gives any sort of in game input"""
        self._play_sound('sounds/menubutton.mp3')

    def zombie_attack_inside(self):
        """plays when a zombie is inside a building"""
        zombie_inside_path = ['sounds/zombieattack1inside.mp3',
                              'sounds/zombieattack2inside.mp3',
                              'sounds/zombieattack3inside.mp3',
                              'sounds/monster_screech.wav',
                              'sounds/breathe_ghost_eerie.wav',
                              ]
        self._play_sound(choice(zombie_inside_path))

    def zombie_attack_outside(self):
        """plays when a zombie is outside a building"""
        zombie_outside_path = ['sounds/zombieattack1inside.mp3',
                               'sounds/zombieattack2inside.mp3',
                               'sounds/zombieattack3inside.mp3',
                               'sounds/monster_ghost_death.wav',
                               'sounds/breathe_ghost_eerie.wav',
                               ]
        self._play_sound(choice(zombie_outside_path))

    def parkview_entrance(self):
        """plays in ch1"""
        self._play_sound('sounds/spooky_werewolf_howl.wav')

    def climatic(self):
        """plays when the tension is building"""
        climatic_paths = ['sounds/climatic.wav',
                          'sounds/action_riser.wav',
                          ]
        self._play_sound(choice(climatic_paths))

    def set_volume(self, level):
        """sets the players' volume of choice"""
        self.volume_level = level

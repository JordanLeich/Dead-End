"""This file is made for easily adding to the chapter files in terms of adding more to the story/game.
Simply just copy and paste this code into the chapter file you are working on and pay close attention
to the comments."""
from choices import _player_choice
from game import player1, sounds
from other.colors import print_green, print_sleep


def name_of_the_area(self):
    """Add whichever checkpoint save this is here or valuable/useful info about this area of the game."""
    player1.checkpoint_save('')  # add the checkpoint number here.
    print_sleep('Story...\n', 2)
    choices = [str(x) for x in range(1, 3)]
    choice_options = [
        'You can either do (1) this or (2) that : ']
    choice = _player_choice(choices, choice_options)
    if choice == '1':
        sounds.zombie_attack_inside()  # play a sound based on the environment or scenario.
        print_sleep('Story effects of picking option 1...\n', 2)

        if not player1.user_attack():  # use this if the player gets in contact with enemies and need to attack.
            return
        player1.total_kills += 1  # set number to however many people or zombies the players successfully kills.
        print_green('You have successfully killed the enemy!\n', 1)
        self.next_area()  # use this if the player is going to a new location or area.
    elif choice == '2':
        print_sleep('Story effects of picking option 2...\n', 2)
        self.next_area()  # use this if the player is going to a new location or area.

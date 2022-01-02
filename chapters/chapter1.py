""" This file holds all the chapter 1 areas of the game. """
from time import sleep
# from classes import Player, Difficulty
from chapters.chapter import Chapter
from chapters.chapter2 import Chapter2

from other.sounds_effects import GameSounds
from game import player1, sounds, Difficulty
from choices import _player_choice, error_message
from other.colors import print_green, print_yellow, print_red, print_sleep, print_blue


class Chapter1(Chapter):
    """Contains all the main chapter 1 areas of the game."""
    chapter_num = 1

    def checkpoints(self):
        """runs movement to levels -- checkpoint when leaving area"""
        return {'0': self.game,
                '1': self.outside_area,
                '2': self.diner_area,
                '3': self.gas_station,
                '4': self.parkview_area,
                '5': self.broken_roads_area,
                '6': self.good_ending_and_continue,
                '7': self.bad_ending,
                }

    def good_ending_and_continue(self):
        """Simply plays the good ending scene and then drops the player into chapter 2."""
        self.good_ending()
        Chapter2.game()

    def game(self):
        """Intro section of the game that begins in the apartment room, checkpoint area # 0"""
        self.start()
        player1.chapter = 1
        if player1.health <= 0:
            print_red('You currently have no health left...\n', 1)
            player1.check_point = f'{player1.check_point}bad'
        elif player1.health >= 500:
            player1.print_achievement(('1', 'Rare'))

        if 250 <= player1.balance <= 999:
            player1.print_achievement(('5', 'Rare'))

        if player1.balance >= 1000:
            player1.print_achievement(('2', 'Ultra Rare'))

        print(
            'You have ended up in a small local town called Hinesville. This old town contains a population of about\n'
            'only 6000 people and holds only a Gas Station, Diner, and a Park. The current year is 1999 and you\n'
            'cannot wait to finally get on with your life and move somewhere more alive\n')
        sleep(2)
        choices = [str(x) for x in range(1, 4)]
        choice_options = [
            'While sitting down in the living room of your house, you can either (1) Look around (2) Walk outside (3) '
            'Travel down the hidden door in the floor: ']
        choice = _player_choice(choices, choice_options)

        if choice == '1':
            print(
                'You have decided to look around your apartment and decide to grab a concealed knife that you legally\n'
                'are allowed to carry in public areas just in case anything happens...\n')
            sleep(1)
            player1.weapon_dict['0'][2] = True  # no other way to find
            player1.print_achievement(('1', 'Common'))
        elif choice == '2':
            sleep(1)
        elif choice == '3':
            sleep(1)
            self.basement_area()
        player1.checkpoint_save('1')

    def basement_area(self):
        """not given a checkpoint, one of the first areas of chapter 1"""
        print_sleep('You have reached the basement area.\n', 1)
        sounds.horror_sound_effects()
        print_sleep('''After living at your home for awhile now, you've had many supplies and broken utilities stored up 
in your basement. Trailing behind you leads a lurking stench of odor containing of what smells like mold and 
rotten flesh.\n''', 1.5)
        choice_options = ['(1) Search around the basement (2) Forget about the basement and leave: ']
        choice = _player_choice([str(x) for x in range(1, 3)], choice_options)

        if choice == '1':
            print_sleep('Amongst searching the basement, you stumble upon some spare money you forgot you had '
                        'saved up in the basement.\n', 1.5)
            sounds.good_luck()
            print_green(f'You found a total of ${player1.get_money()} dollars!\n', 1)
        elif choice == '2':
            sounds.wind_sound()
            print_sleep('''Upon leaving the basement, you head out into the outside area for a breath of fresh air after 
consuming the moldy and old smells of the basement.\n''', 2)

    def gas_station(self):
        """checkpoint area # 3"""
        sounds.horror_sound_effects()
        print_sleep('You have entered the local Gas Station...\n', 1)

        print(
            'From the front counter, you see a man who points his gun at you while you walk in! The man tells you to\n'
            'freeze but then notices that you are a survivor just like him... You both discuss and try to figure out\n'
            'what the hell is going on in this city and the man tells you that there has been a bacteria that can \n'
            'contaminated all meat supply chains across the world...\n')
        sleep(6)

        choice_options = [
            'You have the choice to either (1) Keep talking to the man (2) Ask the man for any supplies along your '
            'journey: ']
        user_choice = _player_choice([str(x) for x in range(1, 3)], choice_options)

        if user_choice == '1':
            print('As you keep talking to the man, he starts to tell you about his family and how they would always\n'
                  'venture out to the park with his young daughter and son...\n')
            sleep(2)
            sounds.zombie_attack_inside()
            print_sleep(
                'Out of nowhere, a group of 3 zombies begin to bang on the glass door from which you entered in from...\n',
                2.5)
            sounds.zombie_attack_inside()
            print(
                'While attempting to save you, the man fights off 2 zombies with his pump shotgun and get eaten alive '
                'while saying, RUN! but more zombies come to arise on you...\n')
            sleep(2.5)
            print_sleep('You decide to fight off the zombies in the will of your hopes for living...\n', 1.5)
            if not player1.user_attack():
                return
            player1.total_kills += 3
            print_green('You have successfully defended off the zombies inside the gas station but it was most '
                        'unfortunate the man you found could not make it...\n', 2)
            choice_options = [
                'You have the choice to either (1) Search the all the bodies of zombies and the dead man (2) Head '
                'over to the local Diner: ']
            user_choice = _player_choice([str(x) for x in range(1, 3)], choice_options)

            if user_choice == '1':
                sounds.good_luck()
                print_sleep(
                    f'After searching everybody in the gas station, you manage to find a total of '
                    f'{player1.get_money()} dollars and you then continue your way over to the local Diner...\n', 2)
            player1.checkpoint_save('2')
        elif user_choice == '2':
            sounds.good_luck()
            print_green(f'The man hands over some cash ({player1.get_money()}) dollars.\n', 1.5)
            print_sleep('He tells you about a mysterious lurking salesman who would wonder around the town quite '
                        'often...\n', 2.5)
            print_sleep('The man says that he has not seen him since the apocalypse has happened but keep the money on '
                        'you in-case he shows...\n', 2.5)
            sounds.wind_sound()
            print(
                'You give thanks to the man and exit the local Gas Station and make your way down a tumbled and broken '
                'road... ')
            print('The gleaming fog and ashe outside is giving way to your vision and you see more and more '
                  'unclear... Deep down inside... you know you must go on further...\n')
            sleep(3.5)
            player1.checkpoint_save('2')

    def outside_area(self):
        """checkpoint area # 1"""
        print_sleep('You make your way to the outside area...\n', 1)
        sounds.wind_sound()
        print(
            'You instantly notice something is not right... a dark gloomy fog covers all of the town and you do not '
            'see\na single friendly soul insight... You start to come to a conclusion about where everybody in the '
            'small\ntown of Hinesville has went but nothing is making sense...\n')
        sleep(3.5)
        choice_options = [
            'You have the choice to either (1) Explore the Outside Area (2) Visit the local Gas Station: ']
        user_choice = _player_choice([str(x) for x in range(1, 3)], choice_options)

        if user_choice == '1':
            print(
                'You decide to explore the outside area and along the way, you see a woman bleeding out on the ground\n'
                'with the shape of a man figure hovering over her...\n')
            sleep(2)
            sounds.zombie_attack_outside()
            print_sleep('Lone behold... the figure is eating the woman alive but you are too late to rescue her!\n',
                        1.5)
            choice_options = ['(1) Attack the zombie (2) Avoid the zombie and run to the local Gas Station: ']
            user_choice = _player_choice([str(x) for x in range(1, 3)], choice_options)

            if user_choice == '1':
                sounds.zombie_attack_outside()
                if not player1.user_attack():
                    return
                player1.total_kills += 1
                sounds.good_luck()
                print_sleep(
                    f'You then search the body of the zombie and decaying woman to find a total '
                    f'of {player1.get_money()} Dollars...\n', 2)
                print_sleep('Finally, you get to make your way over to the local Gas Station...\n', 1.5)
            elif user_choice == '2':
                pass
        elif user_choice == '2':
            pass
        player1.checkpoint_save('3')

    def diner_area(self):
        """checkpoint area # 2"""
        sounds.horror_sound_effects()
        print_sleep('You have entered the local Diner...\n', 1)
        choice_options = [
            'You have the choice to either (1) Search inside the Diner Restaurant Area (2) head towards the '
            'Parkview Area: ']
        user_choice = _player_choice([str(x) for x in range(1, 3)], choice_options)

        if user_choice == '1':
            sounds.good_luck()
            print(
                f'After finishing up your entire search of the diner, you find a total of {player1.get_money()} '
                f'dollars and you refresh up on some food and gain a total of {player1.get_health(5, 15)} health!\n')
            sleep(3)
            print('You also manage to find a bloody photograph on the ground and upon looking at the image, you see a '
                  'familiar face...')
            print(
                'You see the face of the man you met earlier at the local Gas Station taking a group family picture!\n')
            sleep(3)
            player1.print_achievement(('1', 'Uncommon'))
            sounds.horror_sound_effects()
            print('Since you are finished exploring and searching the diner area, you proceed on your path to the '
                  'parkview area...\n')
            sleep(3.5)
            player1.checkpoint_save('4')
        elif user_choice == '2':
            sounds.zombie_attack_outside()
            print_red(
                'Upon leaving the diner area, you come across a group of about 5 zombies heading directly towards '
                'you!\n', 1.5)
            if not player1.user_attack():
                return
            player1.total_kills += 5
            print_green(
                'You have successfully defended off the zombies outside the local Diner... You will now head '
                'over to the Parkview Area\n', 2)
            player1.checkpoint_save('4')

    def broken_roads_area(self):
        """checkpoint area # 5"""
        sounds.zombie_attack_outside()
        print('You have reached the broken roads area and managed to find a running vehicle but there are a group of '
              'about 3 zombies surrounding the vehicle... \nThe zombies begin to head directly towards you and you '
              'prepare to fight once more...\n')
        sleep(4.5)
        if not player1.user_attack():
            return
        player1.total_kills += 3
        sounds.horror_sound_effects()
        print_green(
            'You have successfully fought off the zombies surrounding the running vehicle... You then enter the '
            'running vehicle...\nYou manage to put the vehicle into drive and you drive away into the sunrise...\n', 4)
        player1.checkpoint_save('6')

    def parkview_area(self):
        """checkpoint area # 4"""
        sounds.horror_sound_effects()
        print_sleep('You have entered the parkview area...\n', 1)
        sounds.parkview_entrance()
        sleep(2.5)
        print_sleep(
            'Upon arriving to the parkview area, you are still incapable of seeing very much ahead of yourself...\n',
            1.5)
        choice_options = [
            'You have the choice to either (1) Explore the Parkview Area (2) Explore onto the Broken Roads: ']
        user_choice = _player_choice([str(x) for x in range(1, 3)], choice_options)

        if user_choice == '1':
            print('Upon searching the Parkview Area... You come across a deranged man who is killing zombies left and '
                  'right...\n')
            sleep(2)
            choice_options = ['You have the choice to either (1) Help the man (2) Kill the man: ']
            user_choice = _player_choice([str(x) for x in range(1, 3)], choice_options)

            if user_choice == '1':
                sounds.horror_sound_effects()
                print(
                    'In attempts of helping the man, he screams get the hell away from me, I will blow your head off! '
                    'You now prepare to fight him off!\n')
                sleep(2.5)
            elif user_choice == '2':
                player1.health += 15  # Player gets a bonus of 15 HP due to picking the smarter decision to kill the
                # deranged man instead of helping him.
                sounds.bad_luck()

            if not player1.user_attack('man'):  # attack same for both options - only difference is lead up to it
                sounds.bad_luck()
                print_red('The man has killed you and zombies start to feast on your dead decaying flesh...\n', 2)
                return
            player1.total_kills += 1
            print_green(f'You have successfully killed the man! Upon searching his body, you find a total '
                        f'of ${player1.get_money()}!\n', 1)
            sounds.horror_sound_effects()
            print_sleep('You now decide to leave the Parkview Area...\n', 1.5)
            player1.checkpoint_save('5')
        elif user_choice == '2':
            player1.checkpoint_save('5')

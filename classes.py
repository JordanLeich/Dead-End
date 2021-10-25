class Player:
    """This class is to setup the player with all variables needed
    through out the game. If more variables are needed. they can be
    added here."""

    def __init__(self):
        # user attributes
        self.user_balance = 0
        self.user_health = 0
        self.merchant_luck = 0
        self.user_difficulty = 0
        # user weapons, either true or false boolean values
        self.starting_knife = False
        self.ak_47_rifle = False
        self.beretta_pistol = False
        self.baseball_bat = False
        self.rocker_launcher = False

class Player:
    """This class is to setup the player with all variables needed
    through out the game. If more variables are needed. they can be
    added here."""

    def __init__(self, balance=0, health=0, luck=0, difficulty=0, knife=False, rifle=False, pistol=False, bat=False, rpg=False):
        # user attributes
        self.user_balance = balance
        self.user_health = health
        self.merchant_luck = luck
        self.user_difficulty = difficulty
        # user weapons
        self.starting_knife = knife
        self.ak_47_rifle = rifle
        self.beretta_pistol = pistol
        self.baseball_bat = bat
        self.rocket_launcher = rpg
        #  check point location
        self.check_point = ''

    def get_data(self):
        return vars(self)

    def load_data(self, user_data):
        self.user_balance = user_data['user_balance']
        self.user_health = user_data['user_health']
        self.merchant_luck = user_data['merchant_luck']
        self.user_difficulty = user_data['user_difficulty']
        self.starting_knife = user_data['starting_knife']
        self.baseball_bat = user_data['baseball_bat']
        self.beretta_pistol = user_data['beretta_pistol']
        self.ak_47_rifle = user_data['ak_47_rifle']
        self.rocket_launcher = user_data['rocket_launcher']
        self.check_point = user_data['check_point']

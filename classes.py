class Player:
    def __init__(self, user_balance, user_health, merchant_luck, starting_knife, ak_47_rifle, beretta_pistol,
                 baseball_bat, rocker_launcher, user_data_file, user_difficulty):
        # user attributes
        self.user_balance = user_balance
        self.user_health = user_health
        self.merchant_luck = merchant_luck
        self.user_data_file = user_data_file
        self.user_difficulty = user_difficulty
        # user weapons, either true or false boolean values
        self.starting_knife = starting_knife
        self.ak_47_rifle = ak_47_rifle
        self.beretta_pistol = beretta_pistol
        self.baseball_bat = baseball_bat
        self.rocker_launcher = rocker_launcher

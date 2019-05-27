from file import File


class GameStats:
    """Stores statistic data of alien invasion"""

    def __init__(self, game_set):
        """Initiates the statistic data"""
        self.game_set = game_set
        self.reset_stats()
        
        self.file = File()
        
        #starts the alien invasion in a inactive state
        self.game_active = False

        #The hight score can never be reset
        if self.file.read_file():
            self.high_score = self.file.read_file()
        else:
            self.high_score = 0
        
    def reset_stats(self):
        """Starts the data that can change during the game"""
        self.ships_left = self.game_set.ship_limit
        self.score = 0
        self.level = 1
        
        #a flag to know if the alien invasion is paused or not
        self.game_paused = False
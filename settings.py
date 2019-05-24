class GameSettings:
    """A class to keep all game configurations"""

    def __init__(self):
        """Initialize the configurations of the game"""

        #Screen configurations
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (30, 30, 30)

        #Ship configurations
        self.ship_limit = 3

        #Bullet configurations
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 200, 0)
        self.bullets_allowed = 3
        
        #Aliens configurations
        self.fleet_drop_speed = 15
        
        #Scale with the speed gets increased
        self.speedup_scale = 1.1
        
        #Scale with the score gets increased
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        """Initialize the settings that will change during the game"""
        self.ship_speed = 2.5
        self.bullet_speed = 3.5
        self.alien_speed = 1.5
        
        #fleet_direction equals to one represents to the right; -1 represents to the left
        self.fleet_direction = 1
        
        #score
        self.alien_points = 50
        
    def increase_speed(self):
        """Increases the speed of the aliens, ship and bullets, and also the score for each alien"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)    
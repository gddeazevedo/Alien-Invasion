from pygame.font import SysFont
from pygame.sprite import Group
from ship import Ship


class Scoreboard:
    """A class to show the score info"""
    
    def __init__(self, game_set, stats, screen):
        """Initialize the score attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.game_set = game_set
        
        #Font configurations
        self.text_color = (250, 250, 250)
        self.font = SysFont(None, 23)
        
        #Prepara the images of score board
        self.prep_images()
        
    def prep_score(self):
        """Transform the score in a image"""
        rouded_score = int(round(self.stats.score, -1))
        score_str = 'Score: ' + str('{:,}').format(rouded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.game_set.bg_color)
        
        #Shows the score in the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
    def prep_high_score(self):
        """Transform the high score in an image"""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = 'High Score: ' + str('{:,}').format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.game_set.bg_color)
        
        #Centralize the high score in the top center of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
        
    def prep_level(self):
        """Transfom the level in an image"""
        level_str = 'Level: ' + str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.game_set.bg_color)
        
        #Positionate the level under the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
        
    def prep_ships(self):
        """Shows the quantity of ships that have left"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.game_set, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
            
    def prep_images(self):
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
            
    def show_score(self):
        """Draws the score on the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        
        #Draws the spaceships
        self.ships.draw(self.screen)
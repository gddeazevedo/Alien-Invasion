import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class that represents a single alien of the troop"""

    def __init__(self, game_set, screen):
        """Initialize the alien and define your initial position"""
        Sprite.__init__(self)
        self.screen = screen
        self.game_set = game_set

        #Charges the image of the alien and defines its rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #Initiates each new alien next to the top left corner of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Stores the exact position of the alien
        self.x = float(self.rect.x)

    def check_edges(self):
        """Returns True if the alien in on the edge of the screen"""
        screen_rect = self.screen.get_rect()

        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    #Override
    def update(self):
        """Moves the alien to the right or to the left"""
        speed = self.game_set.alien_speed
        direction = self.game_set.fleet_direction
        self.x += speed * direction
        self.rect.x = self.x

    def show_alien(self):
        """Draws the alien in it's current position"""
        self.screen.blit(self.image, self.rect)
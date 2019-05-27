import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    """A class to menage the space back ground image"""

    def __init__(self, game_set, screen):
        Sprite.__init__(self)
        self.game_set = game_set
        self.screen = screen
        
        self.image = pygame.image.load('images/space.png')
        self.rect = self.image.get_rect()
        
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        self.x = float(self.rect.x)
        
    def update(self):
        self.screen.blit(self.image, self.rect)
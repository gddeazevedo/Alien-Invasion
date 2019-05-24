import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class that menages the bullets fired by the ship"""
    
    def __init__(self, game_set, screen, ship):
        """Creates an object for the bullet in the current position of the ship"""
        Sprite.__init__(self)
        self.screen = screen
        
        #Creates a rectangle for the bullet in (0, 0) and, following that, defines the correct position
        self.rect = pygame.Rect(0, 0, game_set.bullet_width, game_set.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        #Stores the position of the bullet with a decimal value
        self.y = float(self.rect.y)
        
        self.color = game_set.bullet_color
        self.speed = game_set.bullet_speed
        
    #Override
    def update(self):
        """Moves the bullet to the top of the screen"""
        #Updates the position of the bullet
        self.y -= self.speed
        
        #Updates the position of the rect
        self.rect.y = self.y
        
    def draw_bullet(self):
        """Draws the bullet on the screen"""
        #pygame.draw.rect(screen_object, color, the_shape)
        pygame.draw.rect(self.screen, self.color, self.rect)
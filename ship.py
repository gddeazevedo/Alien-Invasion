import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    
    def __init__(self, game_set, screen):
        """Initialize the space ship and defines the initial position"""
        Sprite.__init__(self)
        self.screen = screen
        self.game_set = game_set
        
        #Loads the image of the spaceship and gets its rect
        self.image = pygame.image.load('images/ship.bmp') #returns a surface that represents the ship
        self.rect = self.image.get_rect()
        
        #Gets the rect of the screen
        self.screen_rect = screen.get_rect()
        
        #Initialize each spaceship on the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        #Stores a decimal value for the center of the ship
        self.center = float(self.rect.centerx)
        
        #Movement flags
        self.moving_right = False
        self.moving_left = False
        
    #Override
    def update(self):
        """Updates the position of the ship according to the flag of movement"""
        #Updates the value of the center of the ship, and not the rectangle
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.game_set.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.center -= self.game_set.ship_speed
        
        #Updates the rect object according to self.center
        self.rect.centerx = self.center
        
    def show_ship(self):
        """Draws the spaceship in your current position"""
        self.screen.blit(self.image, self.rect)
        
    def center_ship(self):
        """Puts the ship in the center of the screen"""
        self.center = self.screen_rect.centerx 
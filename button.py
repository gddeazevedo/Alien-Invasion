import pygame
from pygame.font import SysFont


class Button:
    """A class that represents a button"""
    
    def __init__(self, game_set, screen, msg):
        """Starts the attributes of the button"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        #Define dimension and properties of the button
        self.width, self.height = 500, 50 #self.width, self.height = 200, 50 == self.width = 200
                                                                               #self.height = 50
        self.button_color = (0, 175, 0)
        self.text_color = (255, 255, 255)
        self.font = SysFont(None, 48)
        
        #Creating the rect object of the button and putting it in the center of the screen
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        #The message must be prepared only once
        self.prep_msg(msg)
        
    def prep_msg(self, msg):
        """Transform the string in a image and centralize the text in the button"""
        #render() will create an image with the string
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    def draw_button(self):
        """Draws a button in white, and following that, draws the message"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
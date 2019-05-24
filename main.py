import pygame
from settings import GameSettings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    #Starts the game and creates an object for the screen
    #init() initiates the configurations
    pygame.init() 

    game_set = GameSettings()

    screen_dimensions = (game_set.screen_width, game_set.screen_height)
    screen = pygame.display.set_mode(screen_dimensions)
    #set_mode method returns a object that represents the surface of the entire game screen

    pygame.display.set_caption('Alien Invasion')
    
    msg = 'Play! press "p" to start'
    
    #Creates a Play button
    play_button = Button(game_set, screen, msg)
    
    #Creatas an instance to store all statistic data
    stats = GameStats(game_set)
    
    #Creates a panel with the socre
    sb = Scoreboard(game_set, stats, screen)
    
    #Creates a file object to store th high score
    

    #Creates the spaceship
    ship = Ship(game_set, screen)

    #Creates a Group which the bullets'll be stored
    bullets = Group()
    
    #Creates a Group which the aliens will be stored
    aliens = Group()
    
    #Creatas a fleet of aliens
    gf.create_fleet(game_set, screen, ship, aliens)

    #Starts the main loop of the game
    while True:
        gf.check_events(game_set, stats, screen, ship, aliens, bullets, play_button, sb)
        
        if stats.game_active:
            ship.update()
            gf.update_bullets(game_set, stats, screen, ship, aliens, bullets, sb)
            gf.update_aliens(game_set, stats, screen, ship, aliens, bullets, sb)
        
        gf.update_screen(game_set, stats, screen, ship, aliens, bullets, play_button, sb)


run_game()
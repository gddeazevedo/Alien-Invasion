import sys
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien
from pygame.sprite import groupcollide
from pygame.sprite import spritecollideany
from file import File


def save_high_score_in_file(stats):
    """Creates a object to deal with the file that keeps the high score"""
    file = File()
    file.write_file(stats)


def check_keyup_events(event, ship):
    """Checks if some key of the keyboard is not pressed"""
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        ship.moving_left = False


def check_keydown_events(event, game_set, stats, screen, ship, aliens, bullets, sb, play_button):
    """Checks if some key of the keyboard is pressed"""
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE or event.key == pygame.K_f:
        fire_bullets(game_set, screen, ship, bullets)
    elif event.key == pygame.K_q:
        save_high_score_in_file(stats)
        sys.exit()
    elif event.key == pygame.K_p and not stats.game_active and not stats.game_paused:
        start_game(game_set, stats, screen, ship, aliens, bullets, sb)
    elif event.key == pygame.K_ESCAPE and not stats.game_paused and stats.game_active:
        pause_game(stats, play_button)
    elif event.key == pygame.K_r and stats.game_paused and not stats.game_active:
        continue_game(stats, play_button)


def fire_bullets(game_set, screen, ship, bullets):
    """Fires a bullet if the limit is not reached"""
    if len(bullets) < game_set.bullets_allowed:
        #Creates a new bullet and add it to the group
        new_bullet = Bullet(game_set, screen, ship)
        bullets.add(new_bullet)


def check_events(game_set, stats, screen, ship, aliens, bullets, play_button, sb):
    """Listens the events of the keyboard and mouse"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_high_score_in_file(stats)
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, game_set, stats, screen, ship, aliens, bullets, sb, play_button)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos() #gets the posision of the mouse
            check_play_button(game_set, stats, screen, ship, aliens, bullets, play_button, mouse_x, mouse_y, sb)


def continue_game(stats, play_button):
    """Continues the paused game"""
    stats.game_paused = False
    stats.game_active = True
    pygame.mouse.set_visible(False)
    play_button.prep_msg('Play! press "p" to start')


def pause_game(stats, play_button):
    """Pauses the game"""
    stats.game_paused = True
    stats.game_active = False
    pygame.mouse.set_visible(True)
    play_button.prep_msg('Paused! click "r" to continue')
       
                 
def start_game(game_set, stats, screen, ship, aliens, bullets, sb):
    """Start the game and reset the game statistics"""
    #restart the game speed
    game_set.initialize_dynamic_settings()
    
    #Hides the mouse cursor
    pygame.mouse.set_visible(False)
        
    #Start over the statistc data of the game
    stats.reset_stats()
    stats.game_active = True
    
    #Restart the score board images
    sb.prep_images()
        
    #Make void the list of aliens and bullets
    empty_bullets_aliens(aliens, bullets)
        
    #Creates a new fleet and put the ship in the conter of the screen
    create_fleet(game_set, screen, ship, aliens)
    ship.center_ship()
            
            
def check_play_button(game_set, stats, screen, ship, aliens, bullets, play_button, mouse_x, mouse_y, sb):
    """Starts the game when the play button is clicked"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        #Start the game and start over the game
        start_game(game_set, stats, screen, ship, aliens, bullets, sb)


def update_screen(game_set, stats, screen, ship, aliens, bullets, play_button, sb):
    """Updates the images on the screen and alterations to the new screen"""
    #Draws again the screen for each loop iteration
    screen.fill(game_set.bg_color) #fills the background color

    #Draws again all bullets behind the ship and the aliens
    #the sprites() method returns a list with all sprites of the bullets group
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    #Shows the spaceship
    ship.show_ship()
    
    #Shows the alien
    aliens.draw(screen)
    
    #Draws the information about the score
    sb.show_score()
    
    if not stats.game_active:
        play_button.draw_button()

    #Let the more recent screen visible
    pygame.display.flip()


def update_bullets(game_set, stats, screen, ship, aliens, bullets, sb):
    """Updates the position of the bullets and deletes the bullets out of the screen"""
    #Updates the position of the bullets
    bullets.update() 

    #Deletes the bullets when they gets out of the screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    
    check_bullet_alien_collisions(game_set, stats, screen, ship, aliens, bullets, sb)  
    
    
def check_high_score(stats, sb):
    """Checks if there is a new high score"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()  
        
        
def start_new_level(game_set, stats, screen, ship, aliens, sb):
    #increases the game speed
    game_set.increase_speed()
        
    #Increase the level
    stats.level += 1
    sb.prep_level()
     
    #creates a new fleet   
    create_fleet(game_set, screen, ship, aliens) 
        

def check_fleet_over(game_set, stats, screen, ship, aliens, bullets, sb):
    """Checks if the fleet is over, if it is create a new fleet and increase speed of the game"""
    if not len(aliens):
        #If the fleet is destroyed, starts a new level
        bullets.empty()
        start_new_level(game_set, stats, screen, ship, aliens,sb)
        
        
def add_points(game_set, stats, aliens, sb, collisions):
    for aliens in collisions.values():
        stats.score += game_set.alien_points * len(aliens)
        sb.prep_score()
        check_high_score(stats, sb)
        
      
def check_bullet_alien_collisions(game_set, stats, screen, ship, aliens, bullets, sb):
    """Checks if some bullet hit an alien"""
    #Checks if some bullet hit an alien
    #if True, erase the alien and the bullet
    #grouocollide returns a dictionary with the key as the first parameter and the value as the second
    collisions = groupcollide(bullets, aliens, True, True)
    
    #if the dictionary exists, if had any collision, add an alien_points to the score 
    #and show it in the score board
    if collisions:
        add_points(game_set, stats, aliens, sb, collisions)
    
    check_fleet_over(game_set, stats, screen, ship, aliens, bullets, sb)
    
                
def get_number_aliens_x(game_set, alien_width):
    """Determinates the number of aliens that fills in a row"""
    #calculate the number of aliens in one line
    available_space_x = game_set.screen_width - (2 * alien_width)
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(game_set, ship_height, alien_height):
    """Determinates the number of lines with aliens that fit on the screen"""
    available_space_y = game_set.screen_height  - (3 * alien_height) - ship_height
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(game_set, screen, aliens, alien_number, row_number):
    """Creates an alien and position it in line"""
    alien = Alien(game_set, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien.x = alien_width * (1 + 2 * alien_number) 
    alien.rect.x = alien.x
    alien.rect.y =  alien_height * (1 + 2 * row_number)
    aliens.add(alien)


def create_fleet(game_set, screen, ship, aliens):
    """Creates a fleet of aliens"""
    
    #The gap between the aliens is equal to the width of an alien
    alien = Alien(game_set, screen)
    
    #The number of aliens that can fit on the available space on the screen
    number_aliens_x = get_number_aliens_x(game_set, alien.rect.width)
    number_rows = get_number_rows(game_set, ship.rect.height, alien.rect.height)
    
    #Creates the alien fleet
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            #Creates an alien and position it in line
            create_alien(game_set, screen, aliens, alien_number, row_number)
            
            
def check_fleet_edges(game_set, aliens):
    """Checks if some alien reached an edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(game_set, aliens)
            break
        
        
def change_fleet_direction(game_set, aliens):
    """Makes all fleet go down and change they direction"""
    for alien in aliens.sprites():
        alien.rect.y += game_set.fleet_drop_speed
    game_set.fleet_direction *= -1
    
    
def empty_bullets_aliens(aliens, bullets):
    """Empties the list of aliens and bullets"""
    aliens.empty()
    bullets.empty()
    
    
def ship_hit(game_set, stats, screen, ship, aliens, bullets, sb):
    """Checks if the ship was hit by any alien"""
    if stats.ships_left > 0:
        #decrements ship_left
        stats.ships_left -= 1
        
        #Updates the painel with the ships left
        sb.prep_ships()
    
        #Empties the list of aliens and bullets
        empty_bullets_aliens(aliens, bullets)
    
        #Creates a new fleet and put the ship in the center of the screen
        create_fleet(game_set, screen, ship, aliens)
        ship.center_ship()
        
        #Makes a pause
        sleep(1.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
    
    
def check_aliens_bottom(game_set, stats, screen, ship, aliens, bullets, sb):
    """Checks if some alien hit the bottom of the screen"""
    screen_rect = screen.get_rect()
    
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #Treats the case in the same way that is done when the ship is hit
            ship_hit(game_set, stats, screen, ship, aliens, bullets, sb)
            break
            
                       
def update_aliens(game_set, stats, screen, ship, aliens, bullets, sb):
    """Checks if the fleet reached some edge and then updates the position of all aliens"""
    check_fleet_edges(game_set, aliens)
    aliens.update()
    
    #Checks if had any collide among the aliens and the ship
    if spritecollideany(ship, aliens):
        ship_hit(game_set, stats, screen, ship, aliens, bullets, sb)
    
    check_aliens_bottom(game_set, stats, screen, ship, aliens, bullets, sb)
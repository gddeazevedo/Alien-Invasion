from pygame.mixer import Sound
import pygame.mixer

class SoundController:
    """A class to menage sound effects"""
    
    def __init__(self):
        pygame.mixer.init()
        self.alien_killed_sound = Sound('musics/invaderkilled.wav')
        self.shoot_sound = Sound('musics/shoot.wav')
        self.explosion_sound = Sound('musics/explosion.wav')
        
    def play_alien_killed_sound(self):
        Sound.play(self.alien_killed_sound)
        
    def play_shoot_sound(self):
        Sound.play(self.shoot_sound)
        
    def play_explosion_sound(self):
        Sound.play(self.explosion_sound)
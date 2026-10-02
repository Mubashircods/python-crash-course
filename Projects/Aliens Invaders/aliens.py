import pygame
from pygame.sprite import Sprite
from settings import Settings


class Alien(Sprite):
    """The main class to creat aliens."""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.original_image = pygame.image.load('images/alien.bmp')
        self.new_size = (self.settings.allien_size)
        self.image = pygame.transform.scale(self.original_image, self.new_size)
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        


    def check_edges(self):
        """Return true when alien is reached at the edge of screen"""
        screen_rect = self.screen.get_rect()
        return(self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
    
    

    def update(self):
        """Update the movement of alien"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
        
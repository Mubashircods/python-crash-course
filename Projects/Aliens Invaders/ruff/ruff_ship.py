import pygame
from ruuf_settings import Settings


class Ship:
    """The main class to creat and adjust ship."""
    def __init__(self, w):
        pygame.init()
        self.screen = w.screen
        self.screen_rect = w.screen.get_rect()
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.settings = Settings()
        

        self.right = False
        self.left = False

    def update_ship(self):
        if self.right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed
        if self.left and   self.rect.left > 0:
            self.rect.x -= self.settings.ship_speed
        


    def blit_ship(self):
        self.screen.blit(self.image, self.rect)

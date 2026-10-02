import pygame
from settings import Settings



class Ship():
    """A class to mennage the ship."""
    def __init__(self, ai_game):
        """Initializing ship and setting this position."""
        self.screen = ai_game.screen
        self.settings = Settings()
        self.screen_rect = ai_game.screen.get_rect()
        original_image = pygame.image.load('images/Spaceship.png')
        new_size = (self.settings.ship_size)
        self.image = pygame.transform.scale(original_image, new_size)
        self.rect = self.image.get_rect()
        """Set ship to center."""
        self.rect.midbottom = self.screen_rect.midbottom

        """Changing rect value from int to float ant asign it to self.x and y"""
        self.rect.x = float(self.rect.x)
        self.rect.y = float(self.rect.y)
        
        """Make loop flages for ship movement"""
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False

    def update(self):
        """Setting left and right movement"""
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_lr_speed
        if self.move_left and self.rect.left > 0:
            self.rect.x -= self.settings.ship_lr_speed
            """Setting up and down movement."""
        if self.move_up and self.rect.top > self.screen_rect.top:
            self.rect.y -= self.settings.ship_ud_speed
        if self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.settings.ship_ud_speed
    
    def center_ship(self):
        """"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    
    def blitme(self):
        """Draw the ship at it current location."""
        self.screen.blit(self.image, self.rect)


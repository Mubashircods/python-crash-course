import pygame
from pygame.sprite import Sprite





class bullit(Sprite):
    """A class to creat bullit"""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullit_color

        """Making rectangle and set the position of sprite bullits"""
        self.rect = pygame.Rect(0, 0, self.settings.bullit_width,
                                self.settings.bullit_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        self.rect.y = float(self.rect.y)


    def update(self):
        """Making the bullit fire."""
        self.rect.y -= self.settings.bullit_speed

    def draw_bullit(self):
        """Draw the bullit."""
        pygame.draw.rect(self.screen,self.color,self.rect)
    

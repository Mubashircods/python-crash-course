import pygame
from pygame.sprite import Sprite
from ruuf_settings import Settings


class Bullets(Sprite):
    """A class to creat bullets"""
    def __init__(self, win):
        super().__init__()
        self.setting = Settings()
        self.screen = win.screen
        self.screen_rect = win.screen.get_rect()

        """Create a rect to set bbullit"""
        self.color = self.setting.bullit_color
        self.rect = pygame.Rect(0, 0, self.setting.bullet_width,
                                    self.setting.bullet_height)
        self.rect.midtop = win.ship.rect.midtop
        
    def _update_bullets(self):
        self.rect.y -= self.setting.bullet_speed
    def _make_bullets(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
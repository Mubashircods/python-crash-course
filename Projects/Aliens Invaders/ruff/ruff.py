import pygame
import sys
from ruff.ruff_ship import Ship
from ruuf_settings import  Settings
from ruff_bullets import Bullets



class Window:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((
            self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Window")
        self.ship = Ship(self)
        self.bg_color = (self.settings.bg_color)
        self.clock = pygame.time.Clock()
        self.bullets = pygame.sprite.Group()
    def open_window(self):
        while True:
            self._check_event()
            self._update_screen()
            self.clock.tick(self.settings.framerate)

    def _check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)
                
    def _check_keydown_event(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.right = True
        if event.key == pygame.K_LEFT:
            self.ship.left = True
        if event.key == pygame.K_SPACE:
            self._fire_bullits()
    def _check_keyup_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.right = False
        if event.key == pygame.K_LEFT:
            self.ship.left = False

    def _fire_bullits(self):
        new_bullets = Bullets(self)
        self.bullets.add(new_bullets)
    def _update_bullits(self):
            self.bullets.update()
            # for bullet in self.bullets.copy():
                # if bullet.rect.bottom >= 0:
                #     self.bullets.remove(bullet)
    
    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.ship.blit_ship()
        self.ship.update_ship()
        for bullet in self.bullets.sprites():
            bullet._update_bullets()
        self._update_bullits()
        pygame.display.flip()




run_w = Window()
run_w.open_window()
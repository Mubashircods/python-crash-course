import sys
from time import sleep
import pygame
from settings import Settings
from ship_state import GameState
from scoreboard import SchoreBord
from button import Button
from ship import Ship
from bullit import bullit
from aliens import Alien


class AliensInvaders:
    """The main Aliens Invaders game class"""
    def __init__(self):
        """Initializing Game """
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((
            self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(self.settings.name)
        self.stats = GameState(self)
        self.sb = SchoreBord(self)
        self.ship = Ship(self)
        self.bulits = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.game_active = False

        self._creat_fleet()
        self.play_button = Button(self, "Play")
        

    def run_game(self):
        """The main game loop."""
        while True:
            self._check_events()
            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_alien()
            self._update_screen()
            self.clock.tick(self.settings.framerate)

    def _check_events(self):    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_play_button(self, mouse_pos):
        button_click =  self.play_button.rect.collidepoint(mouse_pos)
        if button_click and not self.game_active:
            self.settings.initialize_dynamic_setting()
            self.stats.reset_status()
            self.sb.prep_score()
            self.game_active = True
            
            """get rid to old bullets and ship"""
            self.bulits.empty()
            self.aliens.empty()
            self._creat_fleet()
            self.ship.center_ship()
            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.move_left = True
        elif event.key == pygame.K_UP:
            self.ship.move_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.move_down = True
        elif event.key == pygame.K_q:
                    sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullits()

    def _check_keyup_events(self,event):
        if event.key == pygame.K_LEFT:
            self.ship.move_left = False
        elif event.key == pygame.K_RIGHT: 
            self.ship.move_right = False
        elif event.key == pygame.K_UP:
            self.ship.move_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.move_down = False

    def _fire_bullits(self):
        if len(self.bulits) < self.settings.bullets_allow:
            new_bullit = bullit(self)
            self.bulits.add(new_bullit)
            
    def _update_bullets(self):
        """Get rid of bullit"""
        self.bulits.update()
        for bullit in self.bulits.copy():
            if bullit.rect.bottom <= 0:
                self.bulits.remove(bullit)
        self._check_bullet_alien_cullision()

    def _check_bullet_alien_cullision(self):
        """Check the bullit, alien colission"""
        collisions = pygame.sprite.groupcollide(
            self.bulits, self.aliens, True, True
        )
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_point * len(aliens)
            self.sb.prep_score()
        if not self.aliens:
            self.bulits.empty()
            self._creat_fleet()
            self.settings.increase_speed()
    
    def _creat_fleet(self):
        """Make the alien"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        current_x, current_y = alien_width, alien_height        
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._creat_alien(current_x, current_y)
                current_x  += 2 * alien_width
            current_x = alien_width
            current_y += 2 * alien_height

    def _creat_alien(self, x_position, y_position):
            new_alien = Alien(self)
            new_alien.x = x_position
            new_alien.rect.x = x_position
            new_alien.rect.y = y_position
            self.aliens.add(new_alien)

    def _update_alien(self):
        """The mathodto update the position of ship."""
        self._check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        self._check_alien_bottom()


    def _ship_hit(self):
        """Decrease the ship and more ship sdjud=stment"""
        if self.stats.ship_left > 0:
            self.stats.ship_left -= 1
            self.ship.center_ship()
            # sleep
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    
    def _check_alien_bottom(self):
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                break




    def _check_fleet_edges(self):
        """Checking the fleet is true or false and move the alien"""
        for allien in self.aliens.sprites():
            if allien.check_edges():
                self._change_fleet_direction()
                break

            
    def _change_fleet_direction(self):
        """Changing the fleet direction and drop the alien"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1



    def _update_screen(self):        
        self.screen.fill(self.settings.bg_color)
        for bullit in self.bulits.sprites():
            bullit.draw_bullit()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        self.sb.show_score()
        if not self.game_active:
            self.play_button.draw_button()

        pygame.display.flip()


if __name__ == '__main__':
    """Making intance to run the game."""
    ai = AliensInvaders()
    ai.run_game()



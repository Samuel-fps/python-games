import sys
import pygame
from time import sleep

from settings import Settings
from entities.ship import Ship
from entities.bullet import Bullet
from entities.alien import Alien
from entities.GameStats import GameStats

class SpaceInvaders:
    """Main class to control game behavior"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Space invaders")

        self.game_Active = True
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()


    def run_game(self):
        """Game loop"""
        while True:
            self._check_events()

            if self.game_Active:
                self.ship .update()
                self._update_bullets()
                self._update_aliens()
            
            self._update_screen()
            pygame.display.flip()


    def _check_events(self):
        """Check inputs"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self, event):
        """Keydown controller"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()


    def _check_keyup_events(self, event):
        """Keyup controller"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


    def _update_screen(self):
        """Update game screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        pygame.display.flip()


    def _fire_bullet(self):
        """Create and add a new bullet to the group"""
        print("disparando")
        if len(self.bullets) < self.settings.bullet_max:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def _update_bullets(self):
        """Move and delete bullets"""
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)


    def _check_bullet_collisions(self):
        colisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)


    def _create_fleet(self):
        """Create a alien fleet"""

        # Number of aliens row
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        availiable_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = availiable_space_x // (2 * alien_width)

        # Number of rows
        ship_height = self.ship.rect.height
        availiable_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = availiable_space_y // (2 * alien_height)

        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)


    def _create_alien(self, alien_number, row_number):
        """Create an alien"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)


    def _update_aliens(self):
        """Update aliens"""
        self._check_fleet_edges()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        self._check_alien_bottom()


    def _check_fleet_edges(self):
        """Check if any alien is at edge"""
        for alien in self.aliens:
            if alien.check_edges():
                self._change_fleet_direction()
                break

    
    def _change_fleet_direction(self):
        """Change fleet direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


    def _ship_hit(self):
        "Hit controlller"
        self.stats.ship_left -= 1
        if(self.stats.ship_left <= 0):
            self.game_Active = False
        else:
            self.aliens.empty()
            self.bullets.empty()
            
            self._create_fleet()
            self.ship.center_ship()

            sleep(0.5)
        

    def _check_alien_bottom(self):
        """Check if a alien touch the bottom screen"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break


if __name__ == '__main__':
    si = SpaceInvaders()
    si.run_game()
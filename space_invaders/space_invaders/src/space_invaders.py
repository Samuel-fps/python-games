import sys
import pygame

from settings import Settings
from entities.ship import Ship

class SpaceInvaders:
    """Main class to control thegame behavior"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Space invaders")

        self.ship = Ship(self)


    def run_game(self):
        """Game loop"""
        while True:
            self._check_events()
            self.ship.update()
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

if __name__ == '__main__':
    si = SpaceInvaders()
    si.run_game()
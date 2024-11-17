import sys
import pygame

from settings import Settings
from entities.ship import Ship

class SpaceInvaders:
    """Main class to control thegame behavior"""

    def __init__(self):
        pygame.init()
        self.setting = Settings()

        self.screen = pygame.display.set_mode(
            (self.setting.screen_width, self.setting.screen_height))
        pygame.display.set_caption("Space invaders")

        self.ship = Ship(self)


    def run_game(self):
        """Game loop"""
        while True:
            self._check_events()
            self._update_screen()

            pygame.display.flip()

    def _check_events(self):
        """cCheck inputs"""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    def _update_screen(self):
        """Update game screen"""
        self.screen.fill(self.setting.bg_color)
        self.ship.blitme()


if __name__ == '__main__':
    si = SpaceInvaders()
    si.run_game()
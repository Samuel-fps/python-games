import sys
import pygame

from settings import Settings
from ship import Ship

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

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            self.screen.fill(self.setting.bg_color)
            self.ship.blitme()

            pygame.display.flip()

if __name__ == '__main__':
    si = SpaceInvaders()
    si.run_game()
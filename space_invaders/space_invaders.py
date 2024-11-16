import sys
import pygame

class SpaceInvaders:
    """Main class to control thegame behavior"""

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Space invaders")

    def run_game(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            pygame.display.flip()

if __name__ == '__main__':
    si = SpaceInvaders()
    si.run_game()
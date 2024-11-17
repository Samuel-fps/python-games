import pygame

class Ship:
    """ Ship controller"""

    def __init__(self, si_game):
        self.screen = si_game.screen
        self.screen_rect = si_game.screen.get_rect()

        # Load image
        self.image = pygame.image.load('assets/images/ship.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """ Draw ship """
        self.screen.blit(self.image, self.rect)
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Alien controller"""
    def __init__(self, si_game):
        super().__init__()
        self.screen = si_game.screen
        self.settings = si_game.settings

        self.image = pygame.image.load('../assets/images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

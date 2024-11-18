import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Bullet controller"""

    def __init__(self, si_game):
        """Build a bullet in ship position"""
        super().__init__()
        self.screen = si_game.screen
        self.settings = si_game.settings
        self.color = self.settings.bullet_color

        # Position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, 
                                self.settings.bullet_height)
        self.rect.midtop = si_game.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        """Bullet move"""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
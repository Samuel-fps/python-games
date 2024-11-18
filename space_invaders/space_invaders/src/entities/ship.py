import pygame

class Ship:
    """Ship controller"""

    def __init__(self, si_game):
        self.screen = si_game.screen
        self.screen_rect = si_game.screen.get_rect()

        self.setting = si_game.settings

        # Load image
        self.image = pygame.image.load('../assets/images/ship.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

        # Move flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.setting.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.setting.ship_speed
        self.rect.x = self.x

    def blitme(self):
        """Draw ship"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center ship on screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
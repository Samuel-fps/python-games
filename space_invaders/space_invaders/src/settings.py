class Settings:

    def __init__(self):
        """ Init game configuration"""

        # Screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230,230)

        # Ship
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Bullet
        self.bullet_speed = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_max = 6

        # Alien
        self.alien_speed = 2.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

class GameStats:

    def __init__(self, si_game):
        """Game stats"""
        self.settings = si_game.settings
        self.reset_stats()

    def reset_stats(self):
        self.ship_left = self.settings.ship_limit
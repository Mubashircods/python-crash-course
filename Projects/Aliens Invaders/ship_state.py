class GameState:
    """A class to detect the statics of ship"""
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_status()

    def reset_status(self):
        self.ship_left = self.settings.ship_limits
        self.score = 0


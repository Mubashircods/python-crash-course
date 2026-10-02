class Settings:
    """The class consist of all game settings."""
    def __init__(self):
        """Screen Sattings"""
        self.name = "Aliens Invaders"
        self.screen_width = 1000
        self.screen_height = 625
        self.framerate = 85
        self.bg_color = (230,230,230)
        
        
        self.ship_size = (40,60)
        self.ship_limits = 3
        
        self.bullit_width = 3
        self.bullit_height = 15
        self.bullit_color = (0,92,164)
        self.bullets_allow = 15
        self.allien_size = (30,29)
        
        self.fleet_drop_speed = 6
        self.speedpu_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_setting()
        
    def initialize_dynamic_setting(self):
        """Initializing speed"""
        self.ship_lr_speed = 3.5
        self.ship_ud_speed = 2.0
        self.bullit_speed = 3.5
        self.alien_speed = 0.5
        self.fleet_direction = 1
        self.alien_point = 50

    def increase_speed(self):
        self.ship_lr_speed *= self.speedpu_scale
        self.ship_ud_speed *= self.speedpu_scale
        self.bullit_speed *= self.speedpu_scale
        self.alien_speed *= self.speedpu_scale
        """Increasing the score of aliens after next level"""
        self.alien_point = int(self.alien_point * self.score_scale)

class Settings:
    def __init__(self):
        # screen size
        self.width = 1000
        self.height = 600

        # set background color
        self.bg_color = (10, 100, 230)
        self.ship_speed = 0.5

        # Bullet settings
        self.bullet_speed = 0.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        
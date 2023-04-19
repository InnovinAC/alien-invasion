import pygame


class Ship:
    def __init__(self, game):
        """Initialize the ship and set its starting position"""
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
        self.move_right = False
        self.move_left = False

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)



    def update_position(self):
        # update the ship's position
        # Update the ship's x value, not the rect.
        if self.move_right and self.rect.right < self.screen_rect.right - 10:
            self.x += self.settings.ship_speed

        if self.move_left and self.rect.left > 10:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x.
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)


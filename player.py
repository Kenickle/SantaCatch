import pygame


class Player:
    """Manages and creates the player."""

    def __init__(self, sc_game):
        """Initialises the player and sets it's position."""
        self.screen = sc_game.screen
        self.settings = sc_game.settings
        self.screen_rect = sc_game.screen.get_rect()

        #Loads player, rescales it and gets it's rect.
        self.image = pygame.image.load('image assets/player.png')
        self.image = pygame.transform.scale(self.image, (self.settings.transform_width, self.settings.transform_height))
        self.rect = self.image.get_rect()

        #Spawn the player at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        #Store decimal variant of self.rect.x
        self.x = float(self.rect.x)

        #Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the player's position"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.player_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.player_speed

        #Update self.rect.x
        self.rect.x = self.x

    def blitme(self):
        """Create the player."""
        self.screen.blit(self.image, self.rect)

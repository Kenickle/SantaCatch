import pygame
from pygame.sprite import Sprite
from settings import Settings
import random


class Present(Sprite):
    """Represents many presents continuously generating."""

    def __init__(self, sc_game):
        """Initialise the present(s) and set its/their starting position(s)"""
        super().__init__()
        self.screen = sc_game.screen

        self.settings = Settings()

        #Load the image and set it's rect attribute.
        self.image = self.settings.present_image
        self.image = pygame.transform.scale(self.image, (self.settings.present_width, self.settings.present_height))
        self.rect = self.image.get_rect()

        #Start each new present at a random point at the top of the screen.
        self.start_x = random.randint(30, 570)
        self.rect.x = self.start_x
        self.rect.y = self.rect.height

        #Store each present's horizontal position.
        self.y = float(self.rect.y)

    def update(self):
        """Move the presents down"""
        self.y += self.settings.present_speed
        self.rect.y = self.y

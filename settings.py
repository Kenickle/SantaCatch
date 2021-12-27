import pygame

import random


class Settings:
    """What do you think :/"""

    def __init__(self):
        """Init... game settings... :)"""

        #Screen
        self.screen_width = 600
        self.screen_height = 700
        self.bg_color = (50, 50, 50)
        self.icon = "image assets/present.png"
        self.background = "image assets/background.png"

        #Player, please note that by default it is 16x32 pixels.
        self.player_speed = .9
        self.transform_width = 50
        self.transform_height = 130
        self.increment = 10

        #Presents, please note that by default a present is 16x16.
        self.present_speed = .3

        self.present_image = pygame.image.load(random.choice(["image assets/present.png", "image assets/present2.png", "image assets/present3.png", "image assets/present4.png", "image assets/present5.png", "image assets/present6.png", "image assets/present7.png", "image assets/present8.png"]))
        self.present_width = self.present_image.get_rect().width * 2
        self.present_height = self.present_image.get_rect().height * 2

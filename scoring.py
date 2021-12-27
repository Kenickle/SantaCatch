import pygame.font

class Scoreboard:
    """Scores..."""

    def __init__(self, sc_game):
        """Initialise scorekeeping"""
        self.sc_game = sc_game

        self.screen = sc_game.screen
        self.screen_rect = self.screen.get_rect
        self.settings = sc_game.settings

        #Font.
        self.text_colour = (100, 100, 255)
        self.font = pygame.font.Font("fonts/Minecraft.ttf", 35)

        #Prepare initial score img.
        self.prep_score()

    def prep_score(self):
        """Render the score."""
        score_str = str(self.sc_game.points)
        self.score_image = self.font.render(score_str, True, self.text_colour)

        #Display the score!
        self.score_rect = self.score_image.get_rect()
        self.score_rect.topleft = (20, 20)

    def show_score(self):
        """Draw the score :D"""
        self.screen.blit(self.score_image, self.score_rect)

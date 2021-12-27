import sys
import pygame
from player import Player
from settings import Settings
from presents import Present
from scoring import Scoreboard
from mylibs import divide
from button import Button


class SantaCatch:
    """Base of the game."""

    def __init__(self):
        """Creates game window and initialises assets."""
        pygame.init()
        self.settings = Settings()

        """Customising"""

        #Screen
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        #Caption
        pygame.display.set_caption("Santa Catch!")

        #Icon
        self.icon = pygame.image.load(self.settings.icon)
        pygame.display.set_icon(self.icon)

        #Background
        self.background = pygame.image.load(self.settings.background)

        self.win = False
        self.points = 0
        self.player = Player(self)
        self.sb = Scoreboard(self)
        self.button = Button(self)
        self.presents2 = pygame.sprite.Group()
        self.presents = pygame.sprite.Group()
        self._init_present()

    def run_game(self):
        """Starts the game loop."""
        while True:
            #Background image
            self.screen.blit(self.background, (-261.5, 0))

            #Updates
            if not self.win:
                self._update_settings()
                self._update_presents()
                self.player.update()
            elif self.win:
                self.button.draw_button()
                self.presents.empty()
                self.presents2.empty()
            self._update_screen()
            self._check_events()

    def _check_events(self):
        for event in pygame.event.get():
            #QUIT event
            if event.type == pygame.QUIT:
                sys.exit()

            #KEYDOWN events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.player.moving_right = True
                if event.key == pygame.K_LEFT:
                    self.player.moving_left = True

            #KEYUP events
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.player.moving_right = False
                if event.key == pygame.K_LEFT:
                    self.player.moving_left = False

            #MOUSEBUTTONDOWN events
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        button_clicked = self.button.rect.collidepoint(mouse_pos)
        if button_clicked and self.win:
            self.points = 0
            self._init_present()
            self.player.x = self.screen.get_rect().centerx
            self.settings = Settings()
            self.win = False

    def _update_screen(self):
        """A whole-in-two update whoa!"""
        self.player.blitme()
        self.presents.draw(self.screen)
        self.presents2.draw(self.screen)


        #Draw score!!!!
        self.sb.prep_score()
        self.sb.show_score()

        #Update the screen.
        pygame.display.flip()

    def _init_present(self):
        newpresent = Present(self)
        self.presents.add(newpresent)
        newpresent = Present(self)
        self.presents2.add(newpresent)

    def _update_settings(self):
        dividable = divide.int_check(self.points, 100)
        if self.points >= 10000:
            self.win = True
            print("You won!")
        elif self.points == 0:
            pass
        elif dividable and self.speedup:
            self.settings.player_speed += .03
            self.settings.present_speed += .04
            self.speedup = False

    def _update_presents(self):
        """Update all presents in the shower."""
        self.presents.update()
        for present in self.presents:
            if present.rect.y == 690:
                self.presents.remove(present)
                newpresent = Present(self)
                self.presents.add(newpresent)
            elif pygame.sprite.spritecollideany(self.player, self.presents):
                self.presents.remove(present)
                newpresent = Present(self)
                self.presents.add(newpresent)
                self.points += self.settings.increment
                print(self.points)
                self.sb.prep_score()
        self.presents2.update()
        self.presents2.update()
        for present in self.presents2:
            if present.rect.y == 690:
                self.presents2.remove(present)
                newpresent = Present(self)
                self.presents2.add(newpresent)
            elif pygame.sprite.spritecollideany(self.player, self.presents2):
                self.presents2.remove(present)
                newpresent = Present(self)
                self.presents2.add(newpresent)
                self.points += self.settings.increment * 2
                self.speedup = True
                print(self.points)
                self.sb.prep_score()


if __name__ == '__main__':
    #Starts the game.
    sc = SantaCatch()
    sc.run_game()

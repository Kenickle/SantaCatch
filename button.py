import pygame.font

class Button:

    def __init__(self, sc_game):
        """Innit... Button..."""
        self.screen = sc_game.screen
        self.screen_rect = self.screen.get_rect()

        #Set dimensions.
        self.width, self.height = 200, 50
        self.button_colour = (30, 30, 30)
        self.text_colour = (100, 100, 255)

        self.font = pygame.font.Font("fonts/Minecraft.ttf", 35)

        #Build and center the button!
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        #Prepare the button message once
        self.prep_message("Play again")

    def prep_message(self, msg):
        """Render the message into a usable image!"""
        self.msg_image = self.font.render(msg, True, self.text_colour)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.screen_rect.center

    def draw_button(self):
        #Draw a blank button and then add our content.
        self.screen.fill(self.button_colour, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

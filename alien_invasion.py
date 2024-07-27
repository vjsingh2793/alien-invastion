import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """ Overall class to manage game assets and behavior. """

    def __init__(self):
        """ Initialize the game, and create game resources. """
        pygame.init()
        """PyGame's clock should help the game run consistently on the most systems."""
        self.clock = pygame.time.Clock()
        """Set up the game's settings. """
        self.settings = Settings()

        """Set the width and height of the screen. """
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        """Set the background color. """
        self.bg_color = (self.settings.bg_color)

        self.ship = Ship(self)

        """Set the title of the window. """
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """ Start the main loop for the game. """
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # Make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(60)
            self.screen.fill(self.bg_color)
            self.ship.blitme()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
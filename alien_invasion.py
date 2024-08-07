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
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen. """
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def _check_events(self):
        """Respond to keypresses and mouse events. """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Move the ship to the right
                    self.ship.rect.x += 1

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
# all pygame entries that are being used

import pygame


# TODO: make the main game and implement it in main
class Game:
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.PAUSE_KEY, self.UP_KEY, self.DOWN_KEY = False, False, False


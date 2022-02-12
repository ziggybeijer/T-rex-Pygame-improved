import random

import pygame

import texturer
from texturer import Texturer

# filename for initial game
texture_file = 'base_game'
game_textures = Texturer.__init__(texture_file)


class Game:

    def __init__(self, screen_width, game_speed):
        pygame.init()
        self.dino = self.Dino()
        self.cloud = self.Cloud(screen_width, game_speed)
        self.screen_width = screen_width
        self.game_speed = game_speed







from random import randrange as rnd
from itertools import cycle
from random import choice
import pygame
import pygame_menu
import texturer
import logic

print(logic.weGo)

pygame.init()
speed = 4

# displays game window
displayGame = pygame.display.set_mode((600, 300))
pygame.display.set_caption('test', 'test')
clock = pygame.time.Clock()
pygame.display.update()
clock.tick(120)

# home menu
menu = pygame_menu.Menu('T-rex runner The Game', 300, 100)


# set textures according to menu
# texturer.set_textures(textureName)
# initial player state
# playerState = texturer.player_init
# initial ground state
# ground_begin = texturer.ground

# keep the game running


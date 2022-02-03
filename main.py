from random import randrange as rnd
from itertools import cycle
from random import choice
import pygame
import texturer

pygame.init()
speed = 1

#displays game window
displayGame = pygame.display.set_mode((600, 300))
clock = pygame.time.Clock()
playerState = player_init

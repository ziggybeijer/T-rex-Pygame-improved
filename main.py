import ctypes
import pathlib
import pygame
import pygame_gui
import pygame_menu
from dino import Dino
from cloud import Cloud
from game import Game
from obstacles import *
from texturer import Texturer
import logic

pygame.init()

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
texture_file = 'base_game'
game_textures = Texturer(texture_file)


























# get screen size for different screen sizes
user32 = ctypes.windll.user32
# sizeX = user32.GetSystemMetrics(0)
# sizeY = user32.GetSystemMetrics(1)
# sizeY = sizeY - sizeY * 0.0417
sizeX, sizeY = 1200, 800
# size for menus
menuSizeX = sizeX * 0.5
menuSizeY = sizeY * 0.5
# initialise game window
displayGame = pygame.display.set_mode((sizeX, sizeY), pygame.RESIZABLE)
pygame.display.set_caption('The Amazing T-rex Runner', 'The Amazing T-rex Game')

# the 0,0 coord starts at the top left
DINO_LOCATION = pygame.Rect(50, 300, 75, 175)   # variables are (x-coords, y-coords, width, height)
DINO = pygame.draw.rect(displayGame, (255, 0, 0), DINO_LOCATION)
GROUND_LOCATION = pygame.Rect(0, sizeY - 350, 100000, 10000)


# draws menu background
def draw_background():
    background = pygame.image.load(pathlib.Path('dependencies/images/dino-game-background.png'))
    background = pygame.transform.scale(background, (sizeX, sizeY))
    displayGame.blit(background, (0, 0))
    # displayGame.fill((255, 255, 255))


def game_background():
    # background = pygame.image.load()
    # background = pygame.transform.scale(background, (sizeX, sizeY))
    # displayGame.blit(background, (0, 0))
    displayGame.fill((100, 100, 100))


def scroll_background():
    displayGame.scroll(dx=-5, dy=0)
    pygame.time.wait(1000)
    displayGame.scroll(dx=0)


def jumpFunc(location):
    for i in range(-10, 9):
        i = -2 * i
        location = location.move(0, -i)
        pygame.draw.rect(displayGame, (255, 255, 255), location)
    return location


def menuFunc():
    menuAlive = True
    while menuAlive:
        draw_background()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit(10)
            if event.type == pygame.MOUSEBUTTONDOWN:
                print('I\'m pressing a button')

        if mainMenu.is_enabled():
            mainMenu.update(events)
            mainMenu.draw(displayGame)

        clock.tick()
        pygame.display.update()


def gameFunc():
    running = True
    game_background()
    global DINO_LOCATION
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    DINO_LOCATION = jumpFunc(DINO_LOCATION)
                if event.key == pygame.K_ESCAPE:
                    menuFunc()

        game_background()

        pygame.draw.rect(displayGame, (255, 0, 0), GROUND_LOCATION)
        pygame.draw.rect(displayGame, (255, 255, 255), DINO_LOCATION)
        clock.tick(fps)
        pygame.display.update()


def scrollFunc():
    while True:
        scroll_background()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(5)
        pygame.display.update()


# TODO: maybe move all the menu code to a separate file for better organisation


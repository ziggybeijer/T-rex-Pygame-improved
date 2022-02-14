import ctypes
import pathlib
import pygame
import pygame_gui
from dino import Dino
from cloud import Cloud
from obstacles import *
from texturer import Texturer

pygame.init()

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('The T-rex Game')
texture_file = 'base_game'
game_textures = Texturer(texture_file)


def mainLoop():
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles
    run = True
    clock = pygame.time.Clock()
    game_speed = 20
    x_pos_bg = 0
    y_pos_bg = 380
    points = 0
    player = Dino(game_textures)
    cloud = Cloud(SCREEN_WIDTH, game_speed, game_textures)
    font = pygame.font.Font('Assets/font/PressStart2P-Regular.ttf', 20)
    obstacles = []
    death_count = 0

    def score():
        global points, game_speed
        points += 1
        if points % 100 == 0
            game_speed += 1

        text = font.render('Points: ' + str(points), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (1000, 40)
        SCREEN.blit(text, textRect)

    def background():
        global x_pos_bg, y_pos_bg
        image_width = game_textures.BG.get_width()
        SCREEN.blit(game_textures.BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(game_textures.BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            SCREEN.blit(game_textures.BG, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        SCREEN.fill((255, 255, 255))
        userInput = pygame.key.get_pressed()

        player.draw(SCREEN)
        player.update(userInput)

        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(SmallCactus(game_textures.SMALL_CACTI, SCREEN_WIDTH))
            elif random.randint(0, 2) == 1:
                obstacles.append(LargeCactus(game_textures.LARGE_CACTI, SCREEN_WIDTH))
            elif random.randint(0, 2) == 2:
                obstacles.append(Bird(game_textures.BIRD, SCREEN_WIDTH))

        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update(game_speed, obstacles)
            if player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                death_count += 1
                #menu(death_count)

        background()

        cloud.draw(SCREEN)
        cloud.update()

        score()

        clock.tick(60)
        pygame.display.update()

# TODO: clean up this file and make menu functions with their own lööps
# TODO: make and implement the other menu functions

def pauseMenu():
    run = True
    while run:
        SCREEN.fill((255, 255, 255))
        font = pygame.font.Font('Assets/font/PressStart2P-Regular.ttf', 30)
        text = font.render('Press Arrow up or W to Start', True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 20)
        SCREEN.blit(text, textRect)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    mainLoop()
                if event.key ==



















# get screen size for different screen sizes
user32 = ctypes.windll.user32
# sizeX = user32.GetSystemMetrics(0)
# sizeY = user32.GetSystemMetrics(1)
# sizeY = sizeY - sizeY * 0.0417
sizeX, sizeY = 1200, 800

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

# TODO: maybe move all the menu code to a separate file for better organisation


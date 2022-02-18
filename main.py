import pygame
import pygame_gui
from dino import Dino
from cloud import Cloud
from obstacles import *
from texturer import Texturer

pygame.init()
# constants
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
DIFFICULTY_SELECTOR = 1  # difficulty selector takes a numeric value, can be set via the menu
POINT_SPEED_MODIFIER = 100  # POINT_SPEED_MODIFIER takes a numeric value, higher values speed up the game less
POINT_GAIN_MODIFIER = 1  # POINT_GAIN_MODIFIER takes a numeric value, higher values give less points
points = 0
ghost_points = 0
game_speed = 10
x_pos_bg = 0
y_pos_bg = 380
obstacles = []
# pygame constants
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
background_image = pygame.image.load('Assets/images/dino-game-background.png')
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('The T-rex Game')
title_font = pygame.font.Font('Assets/font/PressStart2P-Regular.ttf', 30)
font = pygame.font.Font('Assets/font/PressStart2P-Regular.ttf', 20)
clock = pygame.time.Clock()
# texture file constants
texture_file = 'base_game'
game_textures = Texturer(texture_file)


def draw_text_topleft(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textRect = textobj.get_rect()
    textRect.topleft = (x, y)
    surface.blit(textobj, textRect)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textRect = textobj.get_rect()
    textRect.center = (x, y)
    surface.blit(textobj, textRect)


def mainLoop():  # the loop that plays the game
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles
    run = True
    player = Dino(game_textures)
    cloud = Cloud(SCREEN_WIDTH, game_speed, game_textures)
    # font = pygame.font.Font('Assets/font/PressStart2P-Regular.ttf', 20)
    death_count = 0

    def score():
        global points, game_speed, POINT_SPEED_MODIFIER, POINT_GAIN_MODIFIER, ghost_points
        ghost_points += 1
        if ghost_points == POINT_GAIN_MODIFIER and ghost_points != 0:
            ghost_points -= POINT_GAIN_MODIFIER
            points += 1
        if points >= 500 and points % POINT_SPEED_MODIFIER == 0:
            game_speed += 0.3
            print(game_speed)

        draw_text(('Points :' + str(points)), font, (0, 0, 0), SCREEN, 800, 40)

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
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit(10)

        SCREEN.fill((255, 255, 255))
        user_input = pygame.key.get_pressed()

        player.draw(SCREEN)
        player.update(user_input)

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
                exit(100)
                death_count += 1
                # menu(death_count)

        background()

        cloud.draw(SCREEN)
        cloud.update()

        score()

        clock.tick(60)
        pygame.display.update()

# TODO: make menu functions with their own lööps
# TODO: make and implement the other menu functions
# TODO: difficulty, powerups and texture select
# TODO: very unlikely: pvp


def pauseMenu():  # right now a barebones copy of what is in what.py
    run = True
    while run:
        SCREEN.fill((200, 200, 200))
        # font = pygame.font.Font('Assets/font/PressStart2P-Regular.ttf', 30)
        text = font.render('Press Any Key To Resume', True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 20)
        SCREEN.blit(text, text_rect)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                exit()
            if event.type == pygame.KEYDOWN:
                mainLoop()

        clock.tick(60)
        pygame.display.update()


def mainMenu():  # has to become the true main menu, that goes to all the otehr loops
    run = True
    while run:
        SCREEN.blit(background_image, (0, 0))
        # title_font = pygame.font.Font('Assets/font/PressStart2P-Regular.ttf', 20)
        draw_text_topleft("The T-Rex Runner Game", title_font, (50, 50, 50), SCREEN, 100, 50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                exit()

        clock.tick(60)
        pygame.display.update()


def optionsMenu():
    pass


def textureMenu():
    pass


def deathMenu():
    pass


# difficulty
def set_modifier(selection_input):
    global DIFFICULTY_SELECTOR, POINT_SPEED_MODIFIER, POINT_GAIN_MODIFIER
    if selection_input == 1:  # easy difficulty?
        DIFFICULTY_SELECTOR = 1
        POINT_SPEED_MODIFIER = 400
        POINT_GAIN_MODIFIER = 10
    elif selection_input == 2:
        DIFFICULTY_SELECTOR = 2
        POINT_SPEED_MODIFIER = 200
        POINT_GAIN_MODIFIER = 5
    elif selection_input == 0:
        DIFFICULTY_SELECTOR = 1
        POINT_SPEED_MODIFIER = 100
        POINT_GAIN_MODIFIER = 1


# set different textures as texture file
def set_textures(filename):  # simple function to change the textures the game uses
    global game_textures
    game_textures = Texturer(filename)


# coin system functions
def save_coins():
    pass


def gain_coins():
    pass


def spend_coins():
    pass


# mainMenu()
# mainLoop()
pauseMenu()

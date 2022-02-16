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
background_image = pygame.image.load('Assets/images/dino-game-background.png')
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('The T-rex Game')
texture_file = 'base_game'
game_textures = Texturer(texture_file)
clock = pygame.time.Clock()


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


def mainLoop(): # the loop that plays the game
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles
    run = True
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
        if points % 100 == 0:
            game_speed += 1

        draw_text(('Points :' + str(points)), font, (0, 0, 0), SCREEN, 1000, 40)

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
                # menu(death_count)

        background()

        cloud.draw(SCREEN)
        cloud.update()

        score()

        clock.tick(60)
        pygame.display.update()

# TODO: clean up this file and make menu functions with their own lööps
# TODO: make and implement the other menu functions


def pauseMenu(): # right now a barebones copy of what is in what.py
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
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    mainLoop()
                if event.key == pygame.K_w:
                    mainLoop()

        clock.tick(60)
        pygame.display.update()


def mainMenu(): # has to become the true main menu, that goes to all the otehr loops
    run = True
    while run:
        SCREEN.blit(background_image, (0, 0))
        title_font = pygame.font.Font('Assets/font/PressStart2P-Regular.ttf', 20)
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


# define assets used in menu's




mainMenu()

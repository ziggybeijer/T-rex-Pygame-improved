import ctypes
import pathlib

import pygame
import pygame_menu

import logic


pygame.init()
clock = pygame.time.Clock()
fps = 60
print('0123456789')
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


def jumpFunc(location, ):
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
                    running = False

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
# menus
# menu theme
menuTheme = pygame_menu.themes.Theme(
    background_color=(0, 0, 0, 0),
    title_background_color=(0, 0, 0, 0),
    title_font=(pathlib.Path('dependencies/font/PressStart2P-Regular.ttf')),
    widget_font=(pathlib.Path('dependencies/font/PressStart2P-Regular.ttf')),
    title_font_color=(38, 38, 38),
    widget_font_color=(38, 38, 38),
    selection_color=(10, 10, 10),
    title_font_size=70,
    widget_background_color=(0, 0, 0, 0),
    title_close_button_background_color=(10, 10, 10),
    title_offset=(0, 0),
    title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_UNDERLINE_TITLE,
    widget_alignment=pygame_menu.locals.ALIGN_LEFT,
)
# main menu
mainMenu = pygame_menu.Menu(
    'T-rex runner The Game',
    menuSizeX, menuSizeY,
    theme=menuTheme,
    mouse_motion_selection=True,
    position=(5, 10),
)
# options menu
optionsMenu = pygame_menu.menu.Menu(
    'Options',
    menuSizeX, menuSizeY,
    theme=menuTheme,
    mouse_motion_selection=True,
    position=(5, 10),
    #onclose=exit(2),
)
# pause menu

# make buttons for mainMenu
# TODO: continue on menu layout and logic
mainMenu.add.button('Play', )
mainMenu.add.button('test', )
mainMenu.add.button(optionsMenu.get_title(), optionsMenu)
mainMenu.add.button('Quit', pygame_menu.events.EXIT)
# make buttons for optionsMenu
optionsMenu.add.none_widget('')
optionsMenu.add.dropselect(
    title='Difficulty',
    items=[
        ('Easy', 0),
        ('Medium', 1),
        ('Hard', 2),
        ('Extreme', 3)
    ],
    font_size=30,
    onchange=logic.setmodifier
)
optionsMenu.add.button('Return to Main Menu', )

# set textures according to menu
# texturer.set_textures(textureName)
# initial player state
# playerState = texturer.player_init
# initial ground state
# ground_begin = texturer.ground


# TODO: make logic for beginning game

gameFunc()
# menuFunc()
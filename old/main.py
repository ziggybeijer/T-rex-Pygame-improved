import ctypes
import pathlib

import pygame
import pygame_menu

import logic
from game import Game

g = Game()
clock = pygame.time.Clock()
clockAbsolute = 0


# draws menu background
def draw_background():
    background = pygame.image.load(pathlib.Path('../dependencies/images/dino-game-background.png'))
    background = pygame.transform.scale(background, (sizeX, sizeY))
    gameWindow.blit(background, (0, 0))
    # gameDisplay.fill((255, 255, 255))


def run_game():
    print('f')
    print(pygame_menu.menu.Menu.get_current(mainMenu))


# basic variables
# get screen size for different screen sizes
user32 = ctypes.windll.user32
sizeX = user32.GetSystemMetrics(0)
sizeY = user32.GetSystemMetrics(1)
sizeY = sizeY - sizeY * 0.0417
# size for menus
menuSizeX = sizeX * 0.5
menuSizeY = sizeY * 0.5
# initialise game window
display = pygame.Surface((sizeX, sizeY))
gameWindow = pygame.display.set_mode((sizeX, sizeY), pygame.RESIZABLE)
pygame.display.set_caption('The Amazing T-rex Runner', 'The Amazing T-rex Game')

# TODO: maybe move all the menu code to a separate file for better organisation
# menus
# menu theme
menuTheme = pygame_menu.themes.Theme(
    background_color=(0, 0, 0, 0),
    title_background_color=(0, 0, 0, 0),
    title_font=(pathlib.Path('../dependencies/font/PressStart2P-Regular.ttf')),
    widget_font=(pathlib.Path('../dependencies/font/PressStart2P-Regular.ttf')),
    title_font_color=(38, 38, 38),
    widget_font_color=(38, 38, 38),
    selection_color=(10, 10, 10),
    title_font_size=80,
    widget_font_size=50,
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
    position=(5, 10)
)
# options menu
optionsMenu = pygame_menu.menu.Menu(
    'Options',
    menuSizeX, menuSizeY,
    theme=menuTheme
)
# pause menu

# make buttons for mainMenu
# TODO: continue on menu layout and logic
mainMenu.add.button('')
mainMenu.add.button('Play', run_game())
mainMenu.add.button('')
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
optionsMenu.add.button('Return to Main Menu', optionsMenu.close)

# set textures according to menu
# texturer.set_textures(textureName)
# initial player state
# playerState = texturer.player_init
# initial ground state
# ground_begin = texturer.ground



# TODO: make logic for beginning game
while True:
    events = pygame.event.get()
    clock.tick()
    clockAbsolute = clockAbsolute + clock.get_time()
    draw_background()

    for event in events:
        if event.type == pygame.QUIT:
            g.running, g.playing = False, False

    if mainMenu.is_enabled():
        mainMenu.update(events)
        mainMenu.draw(gameWindow)

    pygame.display.update()

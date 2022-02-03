import pathlib
import pygame, pygame_menu
import texturer
import logic
import ctypes

pygame.init()
speed = 4
hovered = False

# basic game window
# get screen size for different screen sizes
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
sizeX, sizeY = screensize
sizeY = sizeY - sizeY * 0.04166666666666666666666666666667
# size for menus
menuSizeX = sizeX * 0.3
menuSizeY = sizeY * 0.3
# initialise game window
displayGame = pygame.display.set_mode((sizeX, sizeY), pygame.RESIZABLE)
pygame.display.set_caption('The Amazing T-rex Runner', 'The Amazing T-rex Game')
clock = pygame.time.Clock()

# TODO: maybe move all the menu code to a separate file for better organisation
# menus
# make font
PressStartFont = pygame.font.Font(pathlib.Path('dependencies/font/PressStart2P-Regular.ttf'), 7)
# menu theme
menuTheme = pygame_menu.themes.Theme(
    background_color=(0, 0, 0, 0),
    title_background_color=(90, 10, 3),
    title_font=(pathlib.Path('dependencies/font/PressStart2P-Regular.ttf')),
    widget_font=(pathlib.Path('dependencies/font/PressStart2P-Regular.ttf')),
)
# main menu
mainMenu = pygame_menu.Menu(
    'T-rex runner The Game',
    menuSizeX, menuSizeY,
    theme=menuTheme
)
# options menu
optionsMenu = pygame_menu.menu.Menu(
    'Options',
    menuSizeX, menuSizeY,
    theme=menuTheme
)
# make buttons for mainMenu
# TODO: continue on menu layout and logic
mainMenu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)])
mainMenu.add.button(optionsMenu.get_title(), optionsMenu)
mainMenu.add.button('Play', None)
mainMenu.add.button('Quit', pygame_menu.events.EXIT)
# make buttons for optionsMenu
optionsMenu.add.selector


# draws menu background
def draw_background():
    background = pygame.image.load(pathlib.Path('dependencies/images/Lorem_Ipsum.jpg'))
    background = pygame.transform.scale(background, (sizeX, sizeY))
    displayGame.blit(background, (0, 0))

# set textures according to menu
# texturer.set_textures(textureName)
# initial player state
# playerState = texturer.player_init
# initial ground state
# ground_begin = texturer.ground


while True:
    draw_background()
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    if mainMenu.is_enabled():
        mainMenu.update(events)
        mainMenu.draw(displayGame)

    pygame.display.update()

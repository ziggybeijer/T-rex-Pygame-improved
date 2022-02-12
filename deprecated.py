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
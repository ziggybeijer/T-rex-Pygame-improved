import pygame
import pygame_gui


# houses the functions for the menus
class Menu:
    def __init__(self):
        pass

    @staticmethod
    def mainMenu():
        pass

    @staticmethod
    def optionsMenu():
        pass

    @staticmethod
    def textureMenu():
        pass

    @staticmethod
    def pauseMenu(SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT):
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



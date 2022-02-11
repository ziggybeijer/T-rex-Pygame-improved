import pygame
from texturer import Texturer

# filename for initial game
texture_file = 'base_game'
game_textures = Texturer.__init__(texture_file)


class Game:

    def __init__(self):
        pygame.init()
        self.dino = self.Dino()

    class Dino:
        X_POS = 80
        Y_POS = 310
        Y_POS_DUCK = 340
        JUMP_VEL = 8.5

        def __init__(self):
            self.running, self.ducking, self.jumping = True, False, False
            self.run_img = game_textures.RUNNING
            self.duck_img = game_textures.DUCKING
            self.jump_img = game_textures.JUMPING

            self.step_index = 0
            self.jump_vel = self.JUMP_VEL
            self.image = self.run_img[0]
            self.dino_rect = self.image.get_rect()
            self.dino_rect.x = self.X_POS
            self.dino_rect.y = self.Y_POS

        def update(self, userInput):
            if self.running:
                self.run()
            if self.ducking:
                self.duck()
            if self.jumping:
                self.jump()

            if self.step_index >= 10:
                self.step_index = 0

            if (userInput[pygame.K_UP] or userInput[pygame.K_w]) and not self.jumping:
                self.running, self.ducking, self.jumping = False, False, True
            elif (userInput[pygame.K_DOWN] or userInput[pygame.K_s]) and not self.jumping:
                self.running, self.ducking, self.jumping = False, True, False
            elif not (self.jumping and self.ducking):
                self.running, self.ducking, self.jumping = True, False, False

        def run(self):
            self.image = self.run_img[self.step_index // 5]
            self.dino_rect = self.image.get_rect()
            self.dino_rect.x = self.X_POS
            self.dino_rect.y = self.Y_POS
            self.step_index += 1

        def duck(self):
            self.image = self.duck_img[self.step_index // 5]
            self.dino_rect = self.image.get_rect()
            self.dino_rect.x = self.X_POS
            self.dino_rect.y = self.Y_POS_DUCK
            self.step_index += 1

        def jump(self):


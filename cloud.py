import pygame
import random


# creates and handles the cloud object for decoration
class Cloud:
    def __init__(self, screen_width, game_speed, textures):
        self.screen_width = screen_width
        self.game_speed = game_speed
        self.x = self.screen_width + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = textures.CLOUD
        self.width = self.image.get_width()

    def update(self):
        self.x -= self.game_speed
        if self.x < -self.width:
            self.x = self.screen_width + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
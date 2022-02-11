import pathlib
import pygame


class Texturer:
    def __init__(self, filename):
        self.RUNNING = [
            pygame.image.load('Assets/{}/Dino/DinoRun1.png'.format(filename)),
            pygame.image.load('Assets/{}/Dino/DinoRun2.png'.format(filename))
        ]
        self.DUCKING = [
            pygame.image.load('Assets/{}/Dino/DinoDuck1.png'.format(filename)),
            pygame.image.load('Assets/{}/Dino/DinoDuck2.png'.format(filename))
        ]
        self.JUMPING = pygame.image.load('Assets/{}/Dino/DinoJump.png'.format(filename))

        self.SMALL_CACTI = [
            pygame.image.load('Assets/{}/Cactus/SmallCactus1.png'.format(filename)),
            pygame.image.load('Assets/{}/Cactus/SmallCactus2.png'.format(filename)),
            pygame.image.load('Assets/{}/Cactus/SmallCactus3.png'.format(filename))
        ]
        self.LARGE_CACTI = [
            pygame.image.load('Assets/{}/Cactus/LargeCactus1.png'.format(filename)),
            pygame.image.load('Assets/{}/Cactus/LargeCactus2.png'.format(filename)),
            pygame.image.load('Assets/{}/Cactus/LargeCactus3.png'.format(filename))
        ]
        self.BIRD = [
            pygame.image.load('Assets/{}/Bird/Bird1.png'.format(filename)),
            pygame.image.load('Assets/{}/Bird/Bird2.png'.format(filename))
        ]

        self.CLOUD = pygame.image.load('Assets/{}/Other/Cloud.png'.format(filename))
        self.BG = pygame.image.load('Assets/{}/Other/Track.png'.format(filename))



# TODO: finish the logic of setting setting textures give a specific folder
# TODO: make function for animated objects either in this file or a new one
# initialise variables
player_frame_1 = None
player_frame_2 = None
player_frame_3 = None
player_frame_4 = None

cloud = None

obstacle_1 = None
obstacle_2 = None
obstacle_3 = None
obstacle_4 = None

ground = None


# set textures for objects
def set_textures(folderName):
    global player_init
    player_init = Image.open("{foldername}\\player.png".format(foldername=folderName)).convert("RGBA")  # player start
    global player_frame_1
    global player_frame_2
    global player_frame_3
    global player_frame_4
    player_frame_1 = Image.open("{foldername}\\player_frame_1.png".format(foldername=folderName)).convert("RGBA")
    player_frame_2 = Image.open("{foldername}\\player_frame_2.png".format(foldername=folderName)).convert("RGBA")
    player_frame_3 = Image.open("{foldername}\\player_frame_3.png".format(foldername=folderName)).convert("RGBA")
    player_frame_4 = Image.open("{foldername}\\player_frame_4.png".format(foldername=folderName)).convert("RGBA")

    global cloud
    cloud = Image.open("{foldername}\\cloud.png".format(foldername=folderName)).convert("RGBA")

    global obstacle_1
    global obstacle_2
    global obstacle_3
    global obstacle_4
    obstacle_1 = Image.open("{foldername}\\obstacle_1.png".format(foldername=folderName)).convert("RGBA")
    obstacle_2 = Image.open("{foldername}\\obstacle_2.png".format(foldername=folderName)).convert("RGBA")
    obstacle_3 = Image.open("{foldername}\\obstacle_3.png".format(foldername=folderName)).convert("RGBA")
    obstacle_4 = Image.open("{foldername}\\obstacle_4.png".format(foldername=folderName)).convert("RGBA")

    global ground
    ground = Image.open("{foldername}\\ground.png".format(foldername=folderName)).convert("RGBA")
    return

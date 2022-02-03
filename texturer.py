from PIL import Image

# initialise variables to be global
player_init = "hello world"
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


def set_textures(folderName):
    global player_init
    player_init = Image.open("{foldername}\\player.png".format(foldername=folderName)).convert("RGBA")  # player start position
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

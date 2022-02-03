from PIL import Image

def set_textures(filename):
    global player_init
    player_init = Image.open("{filename}\player.png".format(filename=filename)).convert("RGBA") #player start position
    global player_frame_1
    global player_frame_2
    global player_frame_3
    global player_frame_4
    #player_frame_1
    #player_frame_2
    #player_frame_3
    #player_frame_4

    global cloud
    #cloud

    global obstacle_1
    global obstacle_2
    global obstacle_3
    global obstacle_4
    #obstacle_1
    #obstacle_2
    #obstacle_3
    #obstacle_4

    #ground
    return player_init



import pygame, pygame_menu
import texturer


def setmodifier(text, difficulty_modifier):
    # maths for difficulty
    print(text)
    if difficulty_modifier == 0:
        difficulty_modifier = 0.2
    else:
        difficulty_modifier = difficulty_modifier / 5 + 0.2
    print(difficulty_modifier)
    return difficulty_modifier
# TODO: work on difficulty logic and how it affects speed and reward


def setRewards(difficulty_modifier, time):
    if difficulty_modifier is not None:
        pointReward = difficulty_modifier * (time / 1000)
    return pointReward
# TODO: work on point counter in game, find out what works best

# movementSpeed = lambda x: (modifier*100)-70*(clock/30) if clock/300 >= 1 else (modifier*100)-70


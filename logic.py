import pygame, pygame_menu
import texturer


def change_difficulty(difficulty_modifier, clock):
    # maths for difficulty
    modifier = 0.5
    if modifier is not None:
        modifier = difficulty_modifier
    return modifier
# TODO: work on difficulty logic and how it affects speed and reward

# movementSpeed = lambda x: (modifier*100)-70*(clock/30) if clock/300 >= 1 else (modifier*100)-70


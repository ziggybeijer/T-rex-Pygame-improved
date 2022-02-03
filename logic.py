import pygame, pygame_menu
import main

weGo = main.clock

def change_difficulty(difficulty_modifier):
    # maths for difficulty
    modifier = 0.5
    if modifier is not None:
        modifier = difficulty_modifier
    movementSpeed = lambda x: (modifier*100)-70*(main.clock/30) if main.clock/300 >= 1 else (modifier*100)-70


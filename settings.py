'''
Settings for Connect Four. Most code is inspired by Coding with Tim.

'''

import pygame
pygame.init()

WHITE = (250, 250, 250)
BLACK = (0, 0, 0)
RED = (220,20,60)
BLUE = (30,144,255)
YELLOW = (255,215,0)

SCREEN_HEIGHT, SCREEN_WIDTH = 700, 700
HEIGHT, WIDTH = 600, 700
ROWS, COLS = 6, 7

SQUARE_SIZE = HEIGHT // ROWS       #might not keep this, kind of need this to help visualize where the open circles will go

FPS = 120
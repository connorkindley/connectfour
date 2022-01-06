'''
Settings for Connect Four. Most code is inspired by Coding with Tim.
'''

WHITE = (250, 250, 250)
BLACK = (0, 0, 0)
RED = (220,20,60)
BLUE = (30,144,255)
YELLOW = (255,215,0)

SCREEN_HEIGHT, SCREEN_WIDTH = 700, 700
HEIGHT, WIDTH = 600, 700
ROWS, COLS = 6, 7

SQUARE_SIZE = HEIGHT // ROWS       # need this to help visualize where the open circles will go

FPS = 60

PLAY_AGAIN_BOX = (60, 400, 280, 50)     # center at (200, 425)
QUIT_BOX = (450, 400, 100, 50)      # center at (500, 425)

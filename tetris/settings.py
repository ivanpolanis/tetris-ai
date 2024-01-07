import pygame
from os.path import join

vec = pygame.math.Vector2



#Game Size
BLOCK_SIZE = 40
COLS = 10
ROWS = 22
GAME_WIDTH = COLS * BLOCK_SIZE
GAME_HEIGHT = ROWS * BLOCK_SIZE

#Side bar size
SIDEBAR_WIDTH = 200
PREVIEW_HEIGHT_FRACTION = 0.7
SCORE_HEIGHT_FRACTION = 0.3

#Window
PADDING = 20
WINDOW_WIDTH = GAME_WIDTH + SIDEBAR_WIDTH + 3*PADDING
WINDOW_HEIGHT = GAME_HEIGHT + 2*PADDING

#Fonts
FONT=join('.','fonts','joystix-monospace.otf')
FONT_SIZE=18

#Game Logic
INITIAL_SPEED = 1

MOVE_DIRECTION = {"LEFT": (-1,0), "RIGHT": (1,0), "DOWN": (0,-1)}

ROTATE_DIRECTION = {"clockwise": 1, "counter_clockwise": -1}

SCORE_DATA = {1: 40, 2: 100, 3: 300, 4: 1200 }

#Colors
WINDOW='#212121'
BACKGROUND='#404040'
WHITE='#FFFFFF'
GRID_COLOR='#141518'


INIT_POS_OFFSET = vec(BLOCK_SIZE) // 2
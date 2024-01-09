import pygame
from os.path import join


vec = pygame.math.Vector2()

#Game Size
BLOCK_SIZE = 42
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

#icon
ICON_PATH=join('.','assets','icon.png')


#music
MUSIC_PATH=join('.','sound','music.mp3')



#Game Logic
INITIAL_SPEED = 1

MOVE_DIRECTION = {pygame.K_LEFT: (-1,0), pygame.K_RIGHT: (1,0), pygame.K_DOWN: (0,1)}

ROTATE_DIRECTION = {pygame.K_z: 90, pygame.KSCAN_Z: 90, pygame.K_x: 270, pygame.KSCAN_X: 270}

SCORE_DATA = {1: 40, 2: 100, 3: 300, 4: 1200 }

#Colors
WINDOW='#212121'
BACKGROUND='#404040'
WHITE='#FFFFFF'
GRID_COLOR='#141518'


INIT_POS_OFFSET = pygame.math.Vector2(COLS//2 -1 , 1)


FPS = 60


YELLOW = '#f1e60d'
RED = '#e51b20'
BLUE = '#204b9b'
GREEN = '#65b32e'
PURPLE = '#7b217f'
CYAN = '#6cc6d9'
ORANGE = '#f07e13'
GRAY = '#1C1C1C'
LINE_COLOR = '#FFFFFF'



TETROMINOS={
	'T': {'shape': [(0,0), (-1,0), (1,0), (0,-1)], 'color': join('.','assets','purple.png')},
	'O': {'shape': [(0,0), (0,-1), (1,0), (1,-1)], 'color': join('.','assets','yellow.png')},
	'J': {'shape': [(0,0), (0,-1), (0,1), (-1,1)], 'color': join('.','assets','blue.png')},
	'L': {'shape': [(0,0), (0,-1), (0,1), (1,1)], 'color': join('.','assets','pink.png')},
	'I': {'shape': [(0,0), (0,-1), (0,1), (0,2)], 'color': join('.','assets','aqua_green.png')},
	'S': {'shape': [(0,0), (-1,0), (0,-1), (1,-1)], 'color': join('.','assets','green.png')},
	'Z': {'shape': [(0,0), (1,0), (0,-1), (-1,-1)], 'color': join('.','assets','red.png')}
}



import pygame
from os.path import join

vec = pygame.math.Vector2()

#Modes

MODE = {"USER": 1, "AI": 2}
CURRRENT_MODE = MODE["USER"]

#Game Size
BLOCK_SIZE = 42
COLUMNS = 10
ROWS = 22
GAME_WIDTH = COLUMNS * BLOCK_SIZE
GAME_HEIGHT = (ROWS) * BLOCK_SIZE

#Side bar size
SIDEBAR_WIDTH = 200
PREVIEW_HEIGHT_FRACTION = 0.7
SCORE_HEIGHT_FRACTION = 0.3


#Window
PADDING = 20
WINDOW_WIDTH = GAME_WIDTH + SIDEBAR_WIDTH + 3*PADDING
WINDOW_HEIGHT = GAME_HEIGHT + 2*PADDING

#Fonts
FONT=join('.','src','tetris','assets','fonts','joystix-monospace.otf')
FONT_SIZE=18

#icon
ICON_PATH=join('.','src','tetris','assets','icon.png')

#music
MUSIC_PATH=join('.','src','tetris','assets','sound','music.mp3')

#Title
TITLE_PATH=join('.','src','tetris','assets','title.png')

#Speed
UPDATE_START_SPEED = 800
MOVE_WAIT_TIME = 50
ROTATE_WAIT_TIME = 200

#Game Logic
MOVE_DIRECTION = {pygame.K_LEFT: (0,-1), pygame.K_RIGHT: (0,1), pygame.K_DOWN: (1,0)}
ROTATE_DIRECTION = {"clockwise": 90, "counter_clockwise": 270}
SCORE_DATA = {1: 40, 2: 100, 3: 300, 4: 1200 }

#Colors
WINDOW = '#212121'
BACKGROUND = '#404040'
WHITE= '#FFFFFF'
GRID_COLOR='#212121'
LINE_COLOR = '#FFFFFF'
TEXT_COLOR = '#FFFFFF'
PREGAME_BACKGROUND = '#333333'
CHOSEN_OPTION_COLOR = '#600a8d'
UNCHOSEN_OPTION_COLOR = '#902bc6'
START_BUTTON_COLOR = '#2A801A'

#TETROMINOS
INIT_POS_OFFSET = pygame.math.Vector2(0,COLUMNS//2 -1 )
TETROMINOS={
  # 'I': {'shape': [(0,0), (0,-1), (0,1), (0,2),(0,3),(0,4),(0,-2),(0,-3),(0,-4)], 'color': join('.','src','tetris','assets',,'color_blocks''aqua_green.png')},
	'T': {'shape': [(0,0), (-1,0), (1,0), (0,-1)], 'color': join('.','src','tetris','assets','color_blocks','purple.png')},
	'O': {'shape': [(0,0), (-1,0), (0,1), (-1,1)], 'color': join('.','src','tetris','assets','color_blocks','yellow.png')},
	'J': {'shape': [(0,0), (-1,0), (1,0), (1,-1)], 'color': join('.','src','tetris','assets','color_blocks','blue.png')},
	'L': {'shape': [(0,0), (-1,0), (1,0), (1,1)], 'color': join('.','src','tetris','assets','color_blocks','pink.png')},
	'I': {'shape': [(0,0), (0,-1), (0,1), (0,2)], 'color': join('.','src','tetris','assets','color_blocks','aqua_green.png')},
	'S': {'shape': [(0,0), (0,-1), (-1,0), (-1,1)], 'color': join('.','src','tetris','assets','color_blocks','green.png')},
	'Z': {'shape': [(0,0), (0,1), (-1,0), (-1,-1)], 'color': join('.','src','tetris','assets','color_blocks','red.png')}
}
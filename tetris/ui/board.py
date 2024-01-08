import pygame
from settings import *

class Board:

    def __init__(self):
        self.surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
        self.display_surface = pygame.display.get_surface()
        self.surface.fill(BACKGROUND)

        
    def draw_grid(self):
        for col in range(1,COLS):
            x = col*BLOCK_SIZE
            pygame.draw.line(self.surface,GRID_COLOR, (x,0), (x,self.surface.get_height()),1)

        for row in range(1,ROWS):
            y = row*BLOCK_SIZE
            pygame.draw.line(self.surface,GRID_COLOR, (0,y), (self.surface.get_width(),y),1)
    
    def draw_blocks(self, board: list):
        for i in range(COLS):
            for j in range(ROWS):
                if board[j][i]!= None:
                    block=board[j][i]
                    self.display_surface.blit(block.surface, (i*BLOCK_SIZE+PADDING,j*BLOCK_SIZE+PADDING))
        
    def run(self, board: list):
        self.draw_grid()
        self.display_surface.blit(self.surface, (PADDING,PADDING))
        self.draw_blocks(board)
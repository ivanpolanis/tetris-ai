import pygame
from settings import *

class Board:

    def __init__(self):
        self.surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
        self.display_surface = pygame.display.get_surface()
        self.surface.fill(BACKGROUND)
        print(self.surface)
        print(self.display_surface)

        
    def draw_grid(self):
        for col in range(1,COLS):
            x = col*BLOCK_SIZE
            pygame.draw.line(self.surface,GRID_COLOR, (x,0), (x,self.surface.get_height()),1)

        for row in range(1,ROWS):
            y = row*BLOCK_SIZE
            pygame.draw.line(self.surface,GRID_COLOR, (0,y), (self.surface.get_width(),y),1)
    
    # def draw_blocks(self, board: list):
    #     for i in range(ROWS):
    #         for j in range(COLS):
    #             if board[i][j]!= None:
    #                 block=board[i][j]
    #                 # block.fill(board[i][j].primary_color)
    #                 # pygame.draw.line(block, board[i][j].primary_color)
    #                 self.display_surface.blit(block, (i*BLOCK_SIZE+PADDING,j*BLOCK_SIZE+PADDING))
                    
                    
    #                 # self.surface = pygame.Surface((SIDEBAR_WIDTH, GAME_HEIGHT*SCORE_HEIGHT_FRACTION - PADDING))
    #                 # self.rect = self.surface.get_rect(bottomright=(WINDOW_WIDTH - PADDING, WINDOW_HEIGHT - PADDING))
    #                 # self.display_surface = pygame.display.get_surface()
    #     pass
        
    def run(self):
        # self.draw_blocks(board)
        self.draw_grid()
        self.display_surface.blit(self.surface, (PADDING,PADDING))
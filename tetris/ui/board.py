import pygame
from settings import *

class Board:

    def __init__(self):
        self.surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
        self.display_surface = pygame.display.get_surface()
        self.rect = self.surface.get_rect(topleft = (PADDING, PADDING))
        self.surface.fill(BACKGROUND)

        
    def _draw_grid(self):
        for col in range(1,COLUMNS):
            x = col*BLOCK_SIZE
            pygame.draw.line(self.surface,GRID_COLOR, (x,0), (x,self.surface.get_height()),1)

        for row in range(1,ROWS):
            y = row*BLOCK_SIZE
            pygame.draw.line(self.surface,GRID_COLOR, (0,y), (self.surface.get_width(),y),1)
        
    def run(self):
        self._draw_grid()
        self.display_surface.blit(self.surface, (PADDING,PADDING))
        pygame.draw.rect(self.display_surface, LINE_COLOR, self.rect, 2, 2)
        self.surface.fill(BACKGROUND)
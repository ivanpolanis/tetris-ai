import pygame
from tetris.settings import *
from pygame.image import load
from os.path import join

class Preview():
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.surface = pygame.Surface((SIDEBAR_WIDTH, GAME_HEIGHT*PREVIEW_HEIGHT_FRACTION));
        self.rect = self.surface.get_rect(topright=(WINDOW_WIDTH - PADDING,PADDING))
        
        self.piece_images={piece: load(join('.','src','tetris','assets','tetrominos',f'{piece}.png')).convert_alpha() for piece in TETROMINOS.keys()}
        
    def _change_preview(self, next_pieces):
        for i, piece in enumerate(next_pieces):
            piece_image = self.piece_images[piece]
            x=self.surface.get_width()/2
            y=i*self.surface.get_height()/3 + self.surface.get_height()/6
            rect=piece_image.get_rect(center=(x,y))
            self.surface.blit(piece_image, rect)

    def run(self, next_pieces):
        self.surface.fill(BACKGROUND)
        self._change_preview(next_pieces)
        self.display_surface.blit(self.surface, self.rect)
        pygame.draw.rect(self.display_surface, LINE_COLOR, self.rect, 2, 2)

if __name__ == "__main__":
    pass

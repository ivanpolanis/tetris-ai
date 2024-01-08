import pygame
from settings import *
from tetromino import Tetromino
from block import Block

class Preview(pygame.sprite.Sprite):
    def __init__(self):
        self.group=pygame.sprite.Group()
        super().__init__(self.group)
        self.image=None
        self.display_surface = pygame.display.get_surface()
        self.surface = pygame.Surface((SIDEBAR_WIDTH, GAME_HEIGHT*PREVIEW_HEIGHT_FRACTION));
        self.rect = self.surface.get_rect(topright=(WINDOW_WIDTH - PADDING,PADDING))
        self.surface.fill(BACKGROUND)
        
    # def display_pieces(self, shape):
    # 
    #   blocks = TETROMINOS[shape]['shape']
    #   image = TETROMINOS[shape]['color']
    #   self.image = pygame.image.load(image) 
    #   x = self.surface.get_width() / 2
    #   y = self.increment_height / 2 + i * self.increment_height
    #   rect = shape_surface.get_rect(center = (x,y))
    #   self.surface.blit(shape_surface,rect)
        
        # self.pos = Vector2(pos) + INIT_POS_OFFSET
        # self.rect = self.image.get_rect(topleft = self.pos * BLOCK_SIZE)
        
    def change_preview(self, shape):
        blocks=TETROMINOS[shape]['shape']
        color=TETROMINOS[shape]['color']
        for block in blocks:
            aux=Block(block, color, self.group)
            aux.pos.x=self.surface.get_width() // 2
            aux.pos.y=self.surface.get_height() // 4
            rect= self.surface.get_rect(center=aux.pos)
            self.surface.blit(aux.image,rect)
        self.group.update()
        self.group.draw(self.surface)
    
    def run(self):
        self.display_surface.blit(self.surface, self.rect)
        pygame.draw.rect(self.display_surface, LINE_COLOR, self.rect, 2, 2)

if __name__ == "__main__":
    pass

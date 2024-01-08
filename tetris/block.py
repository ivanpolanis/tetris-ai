import pygame
from enum import Enum
from collections import namedtuple
from settings import BLOCK_SIZE, MOVE_DIRECTION, ROTATE_DIRECTION, ROWS, COLS, INIT_POS_OFFSET
from pygame.math import Vector2


class Block(pygame.sprite.Sprite):
    
    def __init__(self, pos: tuple, image, group: pygame.sprite.Group):
        super().__init__(group)
        self.group = group
        self.image = pygame.image.load(image) 
        
        self.pos = Vector2(pos) + INIT_POS_OFFSET
        self.rect = self.image.get_rect(topleft = self.pos * BLOCK_SIZE)



    def set_rect_pos(self):
        # self.rect = self.image.get_rect(topleft=self.pos*BLOCK_SIZE)
        self.rect.topleft = (self.pos.x.__int__() * BLOCK_SIZE,self.pos.y.__int__() * BLOCK_SIZE) 



    def update(self):
        self.set_rect_pos()



    def move(self, direction: Vector2, board: list[list[bool]]):
        if(not self.check_collision(self.pos + direction, board)):
            self.pos += direction
            return True
        self.pos += direction



    def rotate(self, pivot_pos, degrees: int) -> Vector2:
        translated = self.pos - pivot_pos
        rotated = translated.rotate(degrees)
        return rotated + pivot_pos
    

    def check_collision(self, pos: Vector2, board: list[list[bool]]) -> bool:
        return not ((0 <= pos.x < COLS and 0 <= pos.y < ROWS) and not board[pos.x.__int__()][pos.y.__int__()] )

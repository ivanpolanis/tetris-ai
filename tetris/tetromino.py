import pygame
from enum import Enum
from collections import namedtuple
from settings import BLOCK_SIZE, MOVE_DIRECTION, ROTATE_DIRECTION, ROWS, COLS, INIT_POS_OFFSET, TETROMINOS
from block import *
from pygame import Vector2



# class Block:
#     def __init__(self, pos: Point):
#         self.pos = pos + INIT_POS_OFFSET
#         self.primary_color: str = "#00EE00"
#         self.secondary_color: str = "#00FF00"
#         self.surface = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
#         self.surface.fill(self.primary_color)
#         print(type(self.pos))

#     def draw(self):
#         pass



class Tetromino:#self.type.value["image"
    def __init__(self, shape, group: pygame.sprite.Group):
        self.type = shape
        self.blocks = [Block(point, TETROMINOS[shape]["color"], group) for point in TETROMINOS[shape]["shape"]]


    # def rotate(self) -> None:
    #     pivot_pos = self.blocks[0].pos
    #     new_blocks = [block.rotate(pivot_pos) for block in self.blocks]

    #     #METER LA LOGICA DE COLISION DE BLOQUES
        
    #     self.blocks = new_blocks
    #     return
    
    # def move(self, direction: tuple) -> bool:
    #     for block in self.blocks:
    #             new_pos = block.pos + direction
    #             if(block.check_collision(new_pos)):

            
    #     return True
    

    # def check_collision(self, block_positions: list[tuple]) -> bool:
    #     for block in 


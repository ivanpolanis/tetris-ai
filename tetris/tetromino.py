from math import degrees
import pygame
from enum import Enum
from collections import namedtuple
from settings import BLOCK_SIZE, MOVE_DIRECTION, ROTATE_DIRECTION, ROWS, COLS, INIT_POS_OFFSET, TETROMINOS
from block import *
from pygame import Vector2

class Tetromino(pygame.sprite.Sprite):
    def __init__(self, shape, group: pygame.sprite.Group, board: list[list[bool]], current=False):
        self.type = shape
        self.blocks = [Block(point, TETROMINOS[shape]["color"], group) for point in TETROMINOS[shape]["shape"]]
        self.landing = False
        self.current = current
        self.board = board


    def is_occupied(self, pos: Vector2) -> bool:
        return self.board[pos.x.__int__()][pos.y.__int__()]

#falta que rote antihorario
    def rotate(self, direction: int) -> bool:
        degrees = direction
        pivot_pos = self.blocks[0].pos
        new_blocks = [block.rotate(pivot_pos, degrees) for block in self.blocks]

        for pos in new_blocks:
            if(not ((0 <= pos.x < COLS and 0 <= pos.y < ROWS) and not self.board[pos.x.__int__()][pos.y.__int__()] )):
                return False

        for i in range(len(new_blocks)):
            self.blocks[i].pos = new_blocks[i]
        
        return True


    def move(self, direction: Vector2) -> bool:
        for block in self.blocks:
            new_pos = block.pos + direction
            if(not block.check_collision(new_pos, self.board)):
                continue
            else:
                if(direction == Vector2(0,1)):
                    self.landing = True
                return False

        for block in self.blocks:
            block.move(Vector2(direction),self.board)
        return True


    
    

    # def check_collision(self, block_positions: list[tuple]) -> bool:
    #     for block in 


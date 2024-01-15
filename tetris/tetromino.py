from math import degrees
import pygame
from enum import Enum
from collections import namedtuple
from tetris.settings import *
from tetris.block import *
from pygame import Vector2

class Tetromino(pygame.sprite.Sprite):
    def __init__(self, tetris, shape, group: pygame.sprite.Group, board, current=False):
        self.type = shape
        self.blocks = [Block(self, point, TETROMINOS[shape]["color"], group) for point in TETROMINOS[shape]["shape"]]
        self.landing = False
        self.board = board
        self.tetris = tetris


    def is_occupied(self, pos: Vector2) -> bool:
        return self.board[pos.x.__int__()][pos.y.__int__()]


    def rotate(self, direction: int) -> bool:
        if self.type == "O":
            return True
        degrees = direction
        pivot_pos = self.blocks[0].pos
        new_positions = [block.rotate(pivot_pos, degrees) for block in self.blocks]
        
        if(self._check_collision(new_positions)):
            return False

        for i in range(len(new_positions)):
            self.blocks[i].pos = new_positions[i]
        return True


    def move(self, direction: Vector2) -> bool:
        new_positions = [block.pos + direction for block in self.blocks]
        if(not self._check_collision(new_positions)):
            for block in self.blocks:
                block.move(Vector2(direction),self.board)
            return True
            
        if(direction == Vector2(1,0)):
            self.landing = True
        return False

    #return True if there's collision
    def _check_collision(self, block_positions) -> bool:
        return any(map(lambda block, pos: block.check_collision(pos, self.board), self.blocks, block_positions))


    def update(self):
        self.move(Vector2((1,0)))


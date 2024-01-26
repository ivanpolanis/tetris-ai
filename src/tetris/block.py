import pygame
from enum import Enum
from collections import namedtuple
from tetris.settings import *
from pygame.math import Vector2
import random


class Block(pygame.sprite.Sprite):
    
    def __init__(self, tetromino, pos: tuple, image, group: pygame.sprite.Group):
        super().__init__(group)
        self.tetromino = tetromino
        self.current = True
        self.group = group
        self.image = pygame.image.load(image).convert_alpha()
        self.pos = Vector2(pos) + INIT_POS_OFFSET
        self.rect = self.image.get_rect(topleft = self.pos * BLOCK_SIZE)
        
        self.alive = True  # type: ignore
        self.sfx_image = self.image.copy()
        self.sfx_image.set_alpha(110)
        self.sfx_speed = random.uniform(0.2, 0.6)
        self.sfx_cycles = random.randrange(6, 8)
        self.cycle_counter = 0

    def sfx_end_time(self):
        if self.tetromino.tetris.anim_trigger:
            self.cycle_counter += 1
            if self.cycle_counter > self.sfx_cycles:
                self.cycle_counter = 0
                return True

    def sfx_run(self):
        self.image = self.sfx_image
        self.pos.x -= self.sfx_speed
        self.image = pygame.transform.rotate(self.image, pygame.time.get_ticks() * self.sfx_speed)

    def is_alive(self):
        if not self.alive:

            if not self.sfx_end_time():
                self.sfx_run()
            else:
                self.kill()


    def _set_rect_pos(self):
        self.rect.topleft = (self.pos.y.__int__() * BLOCK_SIZE, self.pos.x.__int__() * BLOCK_SIZE) 


    def update(self):
        self._set_rect_pos()
        self.is_alive()



    def move(self, direction: Vector2, board):
        if(not self.check_collision(self.pos + direction, board)):
            self.pos += direction
            return True
        return False



    def rotate(self, pivot_pos, degrees: int) -> Vector2:
        translated = self.pos - pivot_pos
        rotated = translated.rotate(degrees)
        return rotated + pivot_pos
    

    def check_collision(self, pos: Vector2, board) -> bool:
        return not (( pos.x.__int__() < ROWS  and 0 <= pos.y.__int__() < COLUMNS) and not board[max(pos.x.__int__(),0)][pos.y.__int__()] )

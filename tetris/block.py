import pygame
from enum import Enum
from collections import namedtuple
from settings import BLOCK_SIZE, MOVE_DIRECTION, ROTATE_DIRECTION, ROWS, COLS, INIT_POS_OFFSET
from pygame.math import Vector2



class Block(pygame.sprite.Sprite):
    
    def __init__(self, pos: tuple, image, group: pygame.sprite.Group):
        super().__init__(group)
        self.group = group
        self.pos = Vector2(pos) + INIT_POS_OFFSET
        self.image = pygame.image.load(image) 
        self.set_rect_pos()


    def set_rect_pos(self):
        self.rect = self.image.get_rect(topleft=self.pos*BLOCK_SIZE)


    def update(self):
        self.set_rect_pos()



    # def move(self, direction: tuple):
    #     if(self.check_collision(self.pos + Vector2(direction))):
    #         self.pos += direction

    #         return True
    #     self.pos += direction #dsp vemos




    # def rotate(self, pivot_pos):
    #     translated = self.pos - pivot_pos
    #     rotated = translated.rotate(90)
    #     return rotated + pivot_pos
    

    # def check_collision(self, pos: tuple) -> bool:
    #     pos: Vector2 = Vector2(pos)
    #     if(len(pygame.sprite.spritecollide(self, self.group, False)) != 0 or (0 <= pos.x < COLS and 0 <= pos.y < ROWS)):
    #         return False
    #     return True





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

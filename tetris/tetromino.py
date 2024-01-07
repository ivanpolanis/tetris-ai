import pygame
from enum import Enum
from collections import namedtuple
from settings import BLOCK_SIZE, MOVE_DIRECTION, ROTATE_DIRECTION, ROWS, COLS, INIT_POS_OFFSET

Point = namedtuple('Point', 'x, y')



class Block:
    def __init__(self, pos: Point):
        self.pos = pos + INIT_POS_OFFSET
        self.primary_color = "#00EE00"
        self.secondary_color = "#00FF00"
        self.surface = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
        self.surface.fill(self.primary_color)
        

    def draw(self):
        pass


    # def rotate(self, pivot_pos):
    #     translated = self.pos - pivot_pos
    #     rotated = translated.rotate(90)
    #     return rotated + pivot_pos
    
    
    # def move(self, direction: MOVE_DIRECTION):
    #     # if(Block.check_collision(self.pos + direction)):
    #     #     return
    #     self.pos += direction #dsp vemos


    # def check_collision(self, pos: Point) -> bool:
    #     # if(check_block(pos)):
    #     #     return True

    #     if(0 <= pos.x < COLS and 0 <= pos.y < ROWS):
    #         return False
    #     return True




class Shape(Enum):
    I = {
        "primary_color": "#00FFFF",
        "secondary_color": "(200, 200, 200)",
        "blocks": [Block(Point(0,0)), Block(Point(0,1)), Block(Point(0,-1)), Block(Point(0,-2))] 
    }
    O = {
        "primary_color": "#FFFF00",
        "secondary_color": "(200, 200, 200)",
        "blocks": [Block(Point(0,0)), Block(Point(0,-1)), Block(Point(1,0)), Block(Point(1,-1))] 
    }
    J = {
        "primary_color": "#0000FF",
        "secondary_color": "(200, 200, 200)",
        "blocks": [Block(Point(0,0)), Block(Point(-1,0)), Block(Point(0,-1)), Block(Point(0,-2))] 
    }
    L = {
        "primary_color": "#FFF500",
        "secondary_color": "(200, 200, 200)",
        "blocks": [Block(Point(0,0)), Block(Point(1,0)), Block(Point(0,-1)), Block(Point(0,-2))] 
    }
    S = {
        "primary_color": "#00FF00",
        "secondary_color": "(200, 200, 200)",
        "blocks": [Block(Point(0,0)), Block(Point(-1,0)), Block(Point(0,-1)), Block(Point(1,-1))] 
    }
    Z = {
        "primary_color": "#FF0000",
        "secondary_color": "(200, 200, 200)",
        "blocks": [Block(Point(0,0)), Block(Point(1,0)), Block(Point(0,-1)), Block(Point(-1,1))] 
    }
    T = {
        "primary_color": "#800080",
        "secondary_color": "(200, 200, 200)",
        "blocks": [Block(Point(0,0)), Block(Point(1,0)), Block(Point(1,0)), Block(Point(-1,1))] 
    }
    


class Tetromino:
    def __init__(self, type: Shape):
        self.type = type
        self.primary_color = type.value["primary_color"]
        self.secondary_color = type.value["secondary_color"]
        self.blocks = type.value["blocks"]

    # def rotate(self) -> None:
    #     pivot_pos = self.blocks[0].pos
    #     new_blocks = [block.rotate(pivot_pos) for block in self.blocks]

    #     #METER LA LOGICA DE COLISION DE BLOQUES
        
    #     self.blocks = new_blocks
    #     return
    
    # def move(self, direction: MOVE_DIRECTION) -> bool:
    #     for block in self.blocks:
    #         new_pos = block.pos + direction
    #         if(block.check_collision(new_pos)):
    #             return True
    #     for block in self.blocks:
    #         pass
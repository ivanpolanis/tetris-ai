from tabnanny import check
import pygame
import tkinter as tk
from tetromino import Tetromino
from block import Block
import random
from settings import *
from ui.board import Board
from ui.score import Score
from ui.preview import Preview
from pygame import Vector2
import sys
from os.path import join
# from timer import Timer



class Game:
    def __init__(self) -> None:
        # Data
        self.score: int = 0
        self.level: int = 0 
        self.lines: int = 0
        
        
        # Pygame settings
        pygame.display.set_caption("Tetris")
        self.clock = pygame.time.Clock()
        self.surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.display_surface = pygame.display.get_surface()
        
        # Game logic
        self.board: list[list[bool]] = [[False] * ROWS for _ in range(COLS)]
        
        self.down_speed: int = INITIAL_SPEED
        self.timers = {
            
        }
        
        # UI and pygame
        pygame.init()
        self.board_ui = Board()
        self.score_ui = Score()
        self.preview_ui = Preview()
        
        self.sprites = pygame.sprite.Group()


        self.icon = pygame.image.load(ICON_PATH)
        pygame.display.set_icon(self.icon)


        self.music = pygame.mixer.music.load(MUSIC_PATH)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)


        self.next_pieces= [self.get_random_shape() for shape in range(3)]
        self.cur_tetromino: Tetromino = Tetromino(shape = self.get_next_piece(),  group = self.sprites, board = self.board, current = True)
        
                
    def check_lines(self) -> list[int]:
        checked_lines: list[int] = []
        for j in range(ROWS-1,0,-1):
            valid_line = all(self.board[i][j] for i in range(COLS))
            if valid_line:
                checked_lines.append(j)
        for i in range(len(checked_lines)):
            checked_lines[i]+=i;
        return checked_lines


    def delete_line(self, line: int) -> None:
        for i in range(COLS):
            self.board[i][line] = False
        sprites_a_eliminar = [sprite for sprite in self.sprites.sprites() if sprite.rect.y == line * BLOCK_SIZE]
        for sprite in sprites_a_eliminar:
            sprite.kill()


    def move_lines(self, line: int) -> None:
        for i in range(line, 0,-1):
            for j in range(COLS):
                self.board[j][i] = self.board[j][i-1]
                self.board[j][i-1] = False
            sprites_a_repintar = [sprite for sprite in self.sprites.sprites() if sprite.rect.y == (i-1) * BLOCK_SIZE]
            for sprite in sprites_a_repintar:
                sprite.pos.y += 1
        print(self.board[0][19])


    def calculate_score(self,lines: int) -> None:
        self.lines += lines
        self.score += SCORE_DATA[lines] * (self.level + 1)

        if self.lines % 10 == 0:
            self.level +=1
            self.down_speed += 1 #DESPUES SE VERA
        
        self.score_ui.update_score(lines = self.lines,score = self.score,level = self.level)
    
    def check(self) -> None:
        full_lines = self.check_lines()
        qty_lines = len(full_lines)
        if qty_lines == 0:
            return 
        
        print(full_lines) 
        for line in full_lines:
            self.delete_line(line)
            
        for line in full_lines:
            self.move_lines(line)
        
        self.calculate_score(qty_lines)
        
    
    
    def check_landing(self): #terminar
        if(self.cur_tetromino.landing == True):
            for block in self.cur_tetromino.blocks:
                self.board[block.pos.x.__int__()][block.pos.y.__int__()] = True
            self.cur_tetromino = Tetromino(shape = self.get_next_piece(), group = self.sprites, board = self.board)


    def get_random_shape(self):
        return "O"
        # return random.choice(list(TETROMINOS.keys()))
        
    def get_next_piece(self)->str:
        next_shape= self.next_pieces.pop(0)
        self.next_pieces.append(self.get_random_shape())
        return next_shape

    def check_events(self):
        for event in pygame.event.get():
            if((event.type == pygame.QUIT) or (event.type == pygame.K_ESCAPE)):
                pygame.quit()
                sys.exit()
            elif(event.type == pygame.KEYDOWN):
                if(event.key== pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN):
                    self.cur_tetromino.move(MOVE_DIRECTION[event.key])
                elif(event.key == pygame.K_z or event.key == pygame.KSCAN_Z or event.key == pygame.K_x or event.key == pygame.KSCAN_X):
                    self.cur_tetromino.rotate(ROTATE_DIRECTION[event.key])

    def input(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_DOWN]):
            self.cur_tetromino.move(Vector2(MOVE_DIRECTION[pygame.K_DOWN]))
        if (keys[pygame.K_LEFT]):
            self.cur_tetromino.move(Vector2(MOVE_DIRECTION[pygame.K_LEFT]))
        if (keys[pygame.K_RIGHT]):
            self.cur_tetromino.move(Vector2(MOVE_DIRECTION[pygame.K_RIGHT]))


    def run(self):
        while True:
            self.check_landing()
            self.check_events()
            
            self.sprites.update()
            self.check()
            self.surface.fill(WINDOW)

            self.sprites.draw(self.board_ui.surface)

            
            #components
            self.board_ui.run()
            self.score_ui.run()
            self.preview_ui.run(self.next_pieces)

            #update
            pygame.display.update()
            pygame.time.delay(round(INITIAL_SPEED/self.down_speed)+150)
            self.cur_tetromino.update()

            self.clock.tick(FPS)

if __name__ == "__main__":
    game = Game()
    game.run()

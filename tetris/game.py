import pygame
import tkinter as tk
from tetromino import Tetromino
from block import Block
from timer import Timer
import random
from settings import *
from ui.board import Board
from ui.score import Score
from ui.preview import Preview
from pygame import Vector2
import sys
from os.path import join

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
        
        
        # UI and pygame
        pygame.init()
        self.board_ui = Board()
        self.score_ui = Score(score=self.score, level=self.level, lines=self.lines)
        self.preview_ui = Preview()
        self.sprites = pygame.sprite.Group()

        self.icon = pygame.image.load(ICON_PATH)
        pygame.display.set_icon(self.icon)

        self.music = pygame.mixer.music.load(MUSIC_PATH)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)


        self.next_pieces= [self.get_random_shape() for shape in range(3)]
        self.cur_tetromino: Tetromino = Tetromino(shape = self.get_next_piece(),  group = self.sprites, board = self.board, current = True)
        
        self.down_speed = UPDATE_START_SPEED
        self.down_speed_faster = self.down_speed * 0.3
        self.down_pressed = False
        self.timers = {
			'vertical move': Timer(self.down_speed, True, self.move),
			'horizontal move': Timer(MOVE_WAIT_TIME),
			'rotate': Timer(ROTATE_WAIT_TIME),
		}
        
        self.timers['vertical move'].activate()
                
    def check_lines(self) -> list[int]:
        checked_lines: list[int] = []
        for j in range(0,ROWS):
            valid_line = all(self.board[i][j] for i in range(COLS))
            if valid_line:
                checked_lines.append(j)
        return checked_lines

    def move(self):
        self.cur_tetromino.update()

    def delete_line(self, line: int) -> None:
        for i in range(COLS):
            self.board[i][line] = False
        sprites_to_kill = [sprite for sprite in self.sprites.sprites() if sprite.rect.y == line * BLOCK_SIZE]
        for sprite in sprites_to_kill:
            sprite.kill()

    def move_lines(self, line: int) -> None:
        for i in range(line, 0,-1):
            for j in range(COLS):
                self.board[j][i] = self.board[j][i-1]
                self.board[j][i-1] = False
            sprites_to_recolor = [sprite for sprite in self.sprites.sprites() if sprite.rect.y == (i-1) * BLOCK_SIZE]
            for sprite in sprites_to_recolor:
                sprite.pos.y += 1

    def calculate_score(self,lines: int) -> None:
        self.lines += 1
        self.score += SCORE_DATA[lines] * (self.level + 1)

        if self.lines // ((self.level + 1) * 10) > 0:
            self.level += 1
            self.down_speed *= round(self.down_speed * (0.98-((self.level)*0.0025))**(self.level))
            self.timers['vertical move'].duration = self.down_speed
            self.down_speed_faster = self.down_speed * 0.3
            
            self.timers['vertical move'].duration = self.down_speed
            
        self.score_ui.update_score(score=self.score, level=self.level, lines=self.lines)
    
    def check_completed_lines(self) -> None:
        full_lines = self.check_lines()
        qty_lines = len(full_lines)
        if qty_lines == 0:
            return 
        
        print(full_lines) 
        for line in full_lines:
            self.delete_line(line)
            self.move_lines(line)
        
        self.calculate_score(qty_lines)

    def timer_update(self):
        for timer in self.timers.values():
            timer.update()


    def check_landing(self): #terminar
        if(self.cur_tetromino.landing == True):
            if(self.board[4][0]):
                sys.exit(0)
            
            self.speed_up = False
            for block in self.cur_tetromino.blocks:
                self.board[block.pos.x.__int__()][block.pos.y.__int__()] = True
            self.cur_tetromino = Tetromino(shape = self.get_next_piece(), group = self.sprites, board = self.board)

    def get_random_shape(self):
        return random.choice(list(TETROMINOS.keys()))
        
    def get_next_piece(self)->str:
        next_shape= self.next_pieces.pop(0)
        self.next_pieces.append(self.get_random_shape())
        return next_shape

    def _check_close(self):
        for event in pygame.event.get():
            if((event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                pygame.quit()

    def input(self):
        keys = pygame.key.get_pressed()

        # checking horizontal movement
        if not self.timers['horizontal move'].active:
            if keys[pygame.K_LEFT]:
                self.cur_tetromino.move(MOVE_DIRECTION[pygame.K_LEFT])
                self.timers['horizontal move'].activate()
            if keys[pygame.K_RIGHT]:
                self.cur_tetromino.move(MOVE_DIRECTION[pygame.K_RIGHT])	
                self.timers['horizontal move'].activate()

        # check for rotation
        if not self.timers['rotate'].active:
            if keys[pygame.K_UP] or keys[pygame.K_z] or keys[pygame.KSCAN_Z]:
                self.cur_tetromino.rotate(ROTATE_DIRECTION[pygame.K_z])
                self.timers['rotate'].activate()
    
            if keys[pygame.KSCAN_X] or keys[pygame.K_x]:
                self.cur_tetromino.rotate(ROTATE_DIRECTION[pygame.K_x])
                self.timers['rotate'].activate()

		# down speedup
        if not self.down_pressed and keys[pygame.K_DOWN]:
            self.down_pressed = True
            self.timers['vertical move'].duration = self.down_speed_faster

        if self.down_pressed and not keys[pygame.K_DOWN]:
            self.down_pressed = False
            self.timers['vertical move'].duration = self.down_speed

    def run(self):
        while True:
            self.check_landing()
            self._check_close()
            self.input()
            self.timer_update()
            self.check_completed_lines()
            
            self.sprites.update()
            self.surface.fill(WINDOW)
            self.sprites.draw(self.board_ui.surface)
            
            #components
            self.board_ui.run()
            self.score_ui.run()
            self.preview_ui.run(self.next_pieces)

            #update
            pygame.display.update()
            self.clock.tick()


if __name__ == "__main__":
    game = Game()
    game.run()

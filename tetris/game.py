import pygame
import tkinter as tk
import numpy as np
from tetromino import Shape, Tetromino, Block
import random
from settings import COLS, ROWS, INITIAL_SPEED, WINDOW_WIDTH, WINDOW_HEIGHT, SCORE_DATA, MOVE_DIRECTION, WINDOW
from ui.board import Board
from ui.score import Score
from ui.preview import Preview
import sys




class Game:
    def __init__(self) -> None:
        # Data
        self.score: int = 0
        self.level: int = 0 
        self.lines: int  = 0
        
        
        # Pygame settings
        pygame.display.set_caption("Tetris")
        self.clock = pygame.time.Clock()
        self.surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        
        # Game logic
        self.board: list = [[None for _ in range(COLS)] for _ in range(ROWS)]
        
        self.cur_tetromino: Tetromino = Game.get_random_piece()
        self.speed: int = INITIAL_SPEED

        # UI and pygame
        pygame.init()
        self.board_ui = Board()
        self.score_ui = Score()
        self.preview_ui = Preview()

        # icon = pygame.image.load("../assets/tetris.png")
        # pygame.display.set_icon(icon)



    def put_tetromino_block_in_board(self):
        for block in self.cur_tetromino.blocks:
            self.board[block.pos.x][block.pos.y] = block.primary_color


    def check_lines(self) -> list:
        checked_lines = []
        for i in range(ROWS):
            valid_line = all(self.board[i][j] != 0 for j in range(COLS))
            if valid_line:
                checked_lines.append(i)
        return checked_lines


    def delete_line(self, line: int) -> None:
        for i in range(COLS):
            self.board[line][i] = None


    def move_lines(self, line: int) -> None:
        for i in range(line,ROWS-1):
            for j in range(COLS):
                self.board[i][j] = self.board[i+1][j]


    def calculate_score(self,lines:list) -> None:
        self.lines += lines.len()
        self.score += SCORE_DATA(lines.len()) * (self.level + 1)

        if self.lines / 10 > self.level:
            self.level +=1
        
    
    def get_random_piece() -> Tetromino:
        type = random.choice(list(Shape))
        piece = Tetromino(type)
        return piece

    def check_events(self):
        for event in pygame.event.get():
            if((event.type == pygame.QUIT) or (event.type == pygame.K_ESCAPE)):
                pygame.quit()
                sys.exit()
            elif(event.type == pygame.K_LEFT):
                self.cur_tetromino.move(MOVE_DIRECTION["LEFT"])
            elif(event.type == pygame.K_RIGHT):
                self.cur_tetromino.move(MOVE_DIRECTION["RIGHT"])
            elif(event.type == pygame.K_DOWN):
                self.cur_tetromino.move(MOVE_DIRECTION["DOWN"])
            elif(event.type == pygame.K_z or event.type == pygame.K_Z):
                self.cur_tetromino.rotate()
            elif(event.type == pygame.K_x or event.type == pygame.K_X):
                self.cur_tetromino.rotate()


    def run(self):
        while True:
            self.check_events()
            
            #display
            self.surface.fill(WINDOW)
            
            #components
            self.board_ui.run(self.board)
            self.score_ui.run()
            self.preview_ui.run()
            self.tetromino_ui(self.cur_tetromino)
    
            #update
            self.update()


    # def check_block(self, pos: Point) -> bool:
    #     return (self.board[pos.x][pos.y] != 0)

    def update(self):
        pygame.display.update()
        self.cur_tetromino.move(MOVE_DIRECTION["DOWN"])
        pygame.time.delay(1000)


def game_loop():
    pass


if __name__ == "__main__":
    game = Game()
    game.run()
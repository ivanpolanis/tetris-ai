import pygame
import tkinter as tk
from tetromino import Tetromino
from block import Block
import random
from settings import COLS, ICON_PATH, ROWS, INITIAL_SPEED, WINDOW_WIDTH, WINDOW_HEIGHT, SCORE_DATA, MOVE_DIRECTION, WINDOW, INITIAL_SPEED, ICON_PATH, MUSIC_PATH, FPS, ROTATE_DIRECTION, TETROMINOS
from ui.board import Board
from ui.score import Score
from ui.preview import Preview
import sys




class Game:
    def __init__(self) -> None:
        # Data
        self.score: int = 0
        self.level: int = 0 
        self.lines: int = 0
        self.speed: int = 0
        
        
        # Pygame settings
        pygame.display.set_caption("Tetris")
        self.clock = pygame.time.Clock()
        self.surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        
        # Game logic
        self.board: list[list[Block | None]] = [[None] * COLS for _ in range(ROWS)]
        
        self.speed: int = INITIAL_SPEED

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


        self.cur_tetromino: Tetromino = self.get_random_piece()

    def check_lines(self) -> list[int]:
        checked_lines: list[int] = []
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


    def calculate_score(self,lines:list[int]) -> None:
        self.lines += len(lines)
        self.score += SCORE_DATA[len(lines)] * (self.level + 1)

        if self.lines / 10 > self.level:
            self.level +=1
            self.speed += 1 #DESPUES SE VERA

    def get_random_piece(self) -> Tetromino:
        shape = random.choice(list(TETROMINOS.keys()))
        piece = Tetromino(shape, self.sprites)
        return piece

    def check_events(self):
        for event in pygame.event.get():
            if((event.type == pygame.QUIT) or (event.type == pygame.K_ESCAPE)):
                pygame.quit()
                sys.exit()
            # elif(event.type == pygame.K_LEFT or event.type == pygame.K_RIGHT or event.type == pygame.K_DOWN):
            #     self.cur_tetromino.move(MOVE_DIRECTION[event.type])
            # elif(event.type == pygame.K_z or event.type == pygame.KSCAN_Z or event.type == pygame.K_x or event.type == pygame.KSCAN_X):
            #     self.cur_tetromino.rotate(ROTATE_DIRECTION[event.type])

    def run(self):
        while True:
            self.check_events()
            
            #display
            self.surface.fill(WINDOW)
            
            #components
            self.board_ui.run(self.board)
            self.score_ui.run()
            self.preview_ui.run()
            # self.tetromino_ui(self.cur_tetromino)
    
            #update
            self.update()


    # def check_block(self, pos: Point) -> bool:
    #     return (self.board[pos.x][pos.y] != 0)

    def update(self):
        pygame.display.update()
        pygame.display.flip()
        # self.sprites.update()
        self.sprites.draw(self.board_ui.surface)
        self.clock.tick(FPS)
        pygame.time.delay(self.speed)


def game_loop():
    pass


if __name__ == "__main__":
    game = Game()
    game.run()

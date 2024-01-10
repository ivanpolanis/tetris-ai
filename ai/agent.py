import numpy as np
from collections import deque
from settings import *

MAX_MEMORY=100_000
A=1
B=2
C=3

class Agent:
    def __init__(self):
        self.number_of_games = 0
        self.memory = deque(maxlen=MAX_MEMORY)
        # self.
        self.grid=np.zeros((COLUMNS,ROWS), dtype=np.int8)
        # self.positions=

    def evaluate_height(self):
        heights = [np.argmax(self.grid[col, :] != 0) if np.any(self.grid[col, :] != 0) else ROWS - 1 for col in range(COLUMNS)]
        return heights

    def evaluate_holes(self):
        holes = 0
        for col in self.grid:
            isCeiling = False
            for row in col:
                if row:
                    isCeiling = True
                elif isCeiling:
                    holes +=1      
        return holes

    def evaluate_completed_lines(self):
        completed_lines = np.sum(np.all(self.grid, axis=1))
        return completed_lines * 100

    

    def get_state(self):
        pass
        # self.grid, self.position = self.game.get_game_information()

    def get_reward(self) :
        return 1.9

if __name__ =="__main__":
    agent=Agent()
from tetris.game import Game
# from ai.agent import Agent
# import numpy as np
# import pygame

def main():
    # agent=Agent()
    # matrix = np.array([
    #     [0,0,0,0,0,0,0,0,0,0],
    #     [0,0,0,0,0,0,0,0,0,0],
    #     [0,0,1,0,0,1,0,0,0,0],
    #     [0,0,1,1,1,1,1,0,0,0],
    #     [0,0,1,1,1,1,1,0,1,1],
    #     [0,0,1,1,1,1,1,0,1,1],
    #     [1,0,1,1,1,1,1,0,1,1],
    #     [1,1,1,1,1,1,1,0,1,1],
    #     [1,1,0,1,1,1,1,0,1,1]
    #     ])
    # print(agent.evaluate_bumpiness(matrix.shape[0]-agent.evaluate_height(matrix)))
    # matrix = np.array([
    #     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1],
    #     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1],
    #     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1],
    #     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1],
    #     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1],
    #     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1],
    #     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1],
    #     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],
    #     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
    #     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1]
    #])
    # print(agent.evaluate_bumpiness(matrix.shape[0]-agent.evaluate_height(matrix.T)))
    # print((matrix.T.shape[0]-agent.evaluate_height(matrix.T)).sum())
    # print(agent.evaluate_completed_lines(matrix.T))
    # print(agent.evaluate_holes(matrix.T))
    game=Game()
    # while True:
    #     game.run()
    game.run()


if (__name__=="__main__"):
    main()
    
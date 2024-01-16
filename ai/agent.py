import numpy as np
import sys
from collections import deque
from ai.ai_settings import *
from tetris.settings import *
import random
from ai.model import *
from ai.helper import *
from tetris.game import Game


class Agent:
    
    def __init__(self):
        self.n_games = 0
        self.memory = deque(maxlen=MAX_MEMORY) 
        # self.game.run()
        self.epsilon = EPSILON
        self.state_size = 4
        model = Model()
        self.trainer = Trainer(model=model, lr=0.01, gamma=0.8)
        #TODO: instanciar el trainer y el model
        # self.positions=

 
    def remember(self, status, action, reward, next_status, game_over):
        self.memory.append((status, action, reward, next_status, game_over))

    def train_short_memory(self, state, action, reward, next_state, game_over):
        self.trainer.train_step(state, action, reward, next_state, game_over)

    def train_long_memory(self):
        if(len(self.memory) >= BATCH_SIZE):
            mini_sample = random.sample(self.memory, BATCH_SIZE) 
        else:
            mini_sample = self.memory
        
        states, actions, rewards, next_states, game_overs = zip(*mini_sample)
        self.trainer.train_step(states, actions, rewards, next_states, game_overs)

    def predict_value(self, state):
        return self.trainer.model(state)

    def get_best_state(self, states: torch.Tensor): #poner el tipo de retorno
        self.epsilon = max(EPSILON - self.n_games / ((self.n_games+1) ** 0.30999), 1)
        if(random.randint(0, 100) < self.epsilon):
            index = random.randint(0,len(states)-1)
            return list(states.keys())[index],list(states.values())[index]
        
        max_value = None   #Para gonza es un numero (sys.float_info.min)
        best_state = None
        index = 0
        for i, state in enumerate(states.values()):
            value = self.predict_value(torch.unsqueeze(torch.Tensor(state), 0))
            if not max_value or value > max_value:
                max_value = value
                index = i
                best_state = state
        return list(states.keys())[index],best_state



def train():
    #TODO: setear todo
    plot_scores = []
    plot_mean_scores = []
    score, record, total_score = 0, 0, 0
    agent = Agent()
    env =  Game()
    while(True):
        states = env.get_next_states()
        action, best_state = agent.get_best_state(states)
        reward, game_over = env.play_step(action)
        new_state = env.get_state_properties(env.board)
        agent.train_short_memory(best_state, action, reward, new_state, game_over)
        agent.remember(best_state, action, reward, new_state, game_over)

        if game_over:
            # train long memory, plot result
            env.reset()
            agent.n_games += 1
            agent.train_long_memory()
            if score > record:
                record = score
                agent.model.save()
            print('Game', agent.n_games, 'Score', score, 'Record:', record)
            plot_scores.append(score)
            total_score += score
            mean_score = total_score / agent.n_games
            plot_mean_scores.append(mean_score)
            plot(plot_scores, plot_mean_scores)



if __name__ =="__main__":
    train()

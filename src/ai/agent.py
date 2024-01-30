import numpy as np
import sys
from collections import deque
from ai.ai_settings import *
from tetris.settings import *
import random
from ai.model import *
from ai.helper import *


class Agent:
    
    def __init__(self):
        self.n_games = 0
        self.memory = deque(maxlen=MAX_MEMORY) 
        # self.game.run()
        self.epsilon = EPSILON
        self.state_size = 4
        model = Model()
        model.load_state_dict(torch.load(MODEL_PATH))
        self.trainer = Trainer(model=model, lr=0.01, gamma=0.8)
        epsilon_stop_episode = 500
        self.epsilon = 1
        self.epsilon_min = 0
        self.epsilon_decay = (self.epsilon - self.epsilon_min) / (epsilon_stop_episode)
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

    def get_best_state(self, states: torch.Tensor):
        if(random.random() <= self.epsilon):
            index = random.randint(0,len(states)-1)
            return list(states.keys())[index],list(states.values())[index]
        
        max_value = None   #Para gonza es un numero (sys.float_info.min)
        best_state = None
        index = 0
        for state in states.values():
            if state[0]:
                print(state)
        for i, state in enumerate(states.values()):
            value = self.predict_value(torch.unsqueeze(torch.Tensor(state), 0))
            if not max_value or value >= max_value:
                max_value = value
                index = i
                best_state = state
        # print(list(states.keys())[index])
        return list(states.keys())[index], best_state



def train(env):
    #TODO: setear todo
    plot_scores = []
    plot_mean_scores = []
    score, record, total_score = 0, 0, 0
    agent = Agent()
    while(True):
        states = env.get_next_states()
        action, best_state = agent.get_best_state(states)
        reward, game_over = env.play_step(action)
        new_state = env.get_state_properties()
        agent.train_short_memory(best_state, action, reward, new_state, game_over)
        agent.remember(best_state, action, reward, new_state, game_over)
        if reward > 0:
            print(reward)

        if game_over:
            # train long memory, plot result
            agent.n_games += 1
            agent.train_long_memory()
            score = env.score
            if env.score > record:
                record = env.score
                agent.trainer.model.save()
            print('Game', agent.n_games, 'Score', score, 'Record:', record)
            env.reset()
            plot_scores.append(score)
            total_score += score
            mean_score = total_score / agent.n_games
            score = 0
            plot_mean_scores.append(mean_score)
            plot(plot_scores, plot_mean_scores)
        
                    # Update the exploration variable
        if agent.epsilon > agent.epsilon_min:
            agent.epsilon -= agent.epsilon_decay
            
        if agent.n_games % 50 == 0:
            agent.trainer.model.save(file_name="model.pth")



if __name__ =="__main__":
    train()

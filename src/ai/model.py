import torch
import torch.nn as nn
from torch import optim
import os


def _create_weights(m):
    if isinstance(m, nn.Linear):
        nn.init.xavier_uniform_(m.weight)
        nn.init.constant_(m.bias, 0)


class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        
        self.seq1=nn.Sequential(nn.Linear(4,64), nn.ReLU(inplace=True))
        self.seq2=nn.Sequential(nn.Linear(64,64), nn.ReLU(inplace=True))
        self.seq3=nn.Sequential(nn.Linear(64,1))
        self.apply(_create_weights)


    def forward(self, x: torch.Tensor)->torch.Tensor:
        x=self.seq1(x)
        x=self.seq2(x)
        x=self.seq3(x)
        
        return x
    
    def save(self, file_name='model_record.pth'):
        model_folder_path = './model'
        if not os.path.exists(model_folder_path):
            os.makedirs(model_folder_path)

        file_name = os.path.join(model_folder_path, file_name)
        torch.save(self.state_dict(), file_name)

class Trainer:
    def __init__(self, model, lr, gamma):
        self.lr=lr
        self.gamma = gamma
        self.model = model
        self.optimizer = optim.Adam(model.parameters(), lr=self.lr)
        self.loss_function = nn.MSELoss()
        
    def train_step(self, state, action, reward, next_state, game_over):
        state = torch.tensor(state, dtype=torch.float)
        next_state = torch.tensor(next_state, dtype=torch.float)
        action = torch.tensor(action, dtype=torch.float)
        reward = torch.tensor(reward, dtype=torch.float)
        
        if (len(state.shape) == 1):
            state= torch.unsqueeze(state, 0)
            next_state= torch.unsqueeze(next_state, 0)
            action= torch.unsqueeze(action, 0)
            reward= torch.unsqueeze(reward, 0)
            game_over= (game_over, )
            
        pred = self.model(state)
        
        target = pred.clone()
        for idx in range(len(game_over)):
            Q_new = reward[idx]
            if not game_over[idx]:
                Q_new = reward[idx] + self.gamma*torch.max(self.model(next_state[idx]))
            
            target[idx] = Q_new
            
        self.optimizer.zero_grad()
        loss = self.loss_function(target, pred)
        loss.backward()
        
        self.optimizer.step()
    
# if __name__=="__main__":
#     model=Model()
#     trainer=Trainer(model, 0.01, 0.9)
#     trainer.train_step([1,1,1,1],[1,0,0],[1],[1,1,1,1], False)
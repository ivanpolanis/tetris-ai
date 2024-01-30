import torch
from os.path import join

MAX_MEMORY = 10_000
BATCH_SIZE = 1000
EPSILON = 80
HEIGHTS_COEF = -0.510066
LINES_COEF = 1.760666
HOLES_COEF = -0.35663
BUMPINESS_COEF = -0.184483

MODEL_PATH = join('.','model','model.pth')

device = "cuda" if torch.cuda.is_available() else "cpu"
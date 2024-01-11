import torch

MAX_MEMORY = 10_000
BATCH_SIZES = 1000
device = "cuda" if torch.cuda.is_available() else "cpu"
EPSILON = 80
LINES_COEF = -0.510066
HEIGHTS_COEF = 0.760666
HOLES_COEF = -0.35663
BUMPINESS_COEF = -0.184483

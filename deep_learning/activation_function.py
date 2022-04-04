import numpy as np


def step_function(arr: np.array) -> np.array:
  return np.array(arr > 0, dtype=np.int)


def sigmoid(x: np.array) -> np.array:
  return 1 / (1 + np.exp(-x))

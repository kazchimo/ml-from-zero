import numpy as np


def step_function(arr: np.array) -> np.array:
  return np.array(arr > 0, dtype=np.int)


def sigmoid(x: np.array) -> np.array:
  return 1 / (1 + np.exp(-x))


def relu(x: np.array) -> np.array:
  return np.maximum(0, x)


def softmax(x: np.array) -> np.array:
  mx = np.max(x)
  exp_x = np.exp(x - mx)
  exp_sum = np.sum(exp_x)
  return exp_x / exp_sum

import numpy as np


def AND(x1: float, x2: float) -> int:
  x = np.array([x1, x2])
  w = np.array([0.5, 0.5])
  b = -0.7

  if np.sum(w * x) + b <= 0:
    return 0
  else:
    return 1


def NAND(x1: float, x2: float) -> int:
  x = np.array([x1, x2])
  w = np.array([-0.5, -0.5])
  b = 0.7

  if np.sum(w * x) + b <= 0:
    return 0
  else:
    return 1


def OR(x1: float, x2: float) -> int:
  x = np.array([x1, x2])
  w = np.array([0.5, 0.5])
  b = -0.2

  if np.sum(w * x) + b <= 0:
    return 0
  else:
    return 1


def XOR(x1: float, x2: float) -> int:
  s1 = NAND(x1, x2)
  s2 = OR(x1, x2)
  return AND(s1, s2)

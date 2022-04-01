def And(x1: float, x2: float) -> int:
  w1, w2, theta = 0.5, 0.5, 0.7

  if x1 * w1 + x2 * w2 <= theta:
    return 0
  else:
    return 1

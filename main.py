import numpy as np

from deep_learning.activation_function import step_function


def main():
  arr = np.array([5, -5, 0.1])
  results = step_function(arr)


if __name__ == '__main__':
  main()

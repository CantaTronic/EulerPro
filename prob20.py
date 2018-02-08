
from __future__ import print_function
import sys
import numpy as np
import math

def count(strNum):
  numList = np.array([int(ch) for ch in strNum])
  return numList.sum()

def main():
  i = 100
  fact = math.factorial(i)
  print(i,"! =\t", fact,"\t digits = ", count(str(fact)))

if __name__ == "__main__":
  sys.exit(main())

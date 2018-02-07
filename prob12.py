
from __future__ import print_function
import sys
import numpy as np
import math

def getTrgNum(n):
  #return n-th triangular number
  tr_num = np.arange(1, n+1).sum()
  return tr_num

def divisor(number):
  a = np.empty((1), int)
  i = int(math.sqrt(number))
  while (i > 0):
    if (number % i == 0):
      a = np.append(a, i )
      a = np.append(a, number/i)
    i = i - 1
  divNumb = len(a)-1
  return divNumb

def main():
  for i in range (1,1000000):
    tmp = getTrgNum(i)
    divNumb = divisor(tmp)
    print("i = ", i, ", num = ", getTrgNum(i), ", divNum = ", divNumb)
    if (divNumb > 500):
      break
  sys.exit(0)

if __name__ == "__main__":
  sys.exit(main())

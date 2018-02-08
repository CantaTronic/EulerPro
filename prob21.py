
from __future__ import print_function
import sys
import numpy as np
import math

def getPropDivisor(number):
  #proper divisors of n are numbers less than n which divide evenly into n
  a = np.empty((1), int)
  i = int(math.sqrt(number))
  while (i > 0):
    if (number % i == 0):
      a = np.append(a, i )
      if (i*i != number and i != 1):
        a = np.append(a, number/i)
    #print(i, "\t", a[1:])
    i = i - 1
  return a[1:]

def d(num):
  return getPropDivisor(num).sum()

def main():
  am_sum = 0
  for a in range (1, 10000):
    for b in range (1, 10000):
      if (d(a) == b and d(b) == a and a != b):
        print("Find amicable: ", a,"\t", b)
        am_sum += a + b
  print("Result: ", am_sum)
  sys.exit(0)

if __name__ == "__main__":
  sys.exit(main())


'''
Highly divisible triangular number

What is the value of the first triangle number to have over five hundred divisors?

link: https://projecteuler.net/problem=12
'''

from __future__ import print_function
import sys
import numpy as np
import math

def getTrgNum(n):
  #return n-th triangular number
  tr_num = np.arange(1, n+1).sum()
  return tr_num

def divisor(number):
  #count number of divisors
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
  upper_lim = 1000000
  for i in range (1, upper_lim):
    tmp = getTrgNum(i)  #calculate i-th triangular number
    divNumb = divisor(tmp)  #get number of divisors
    #print("i = ", i, ", num = ", getTrgNum(i), ", divNum = ", divNumb)    #debug
    if (divNumb > 500):
      print("Answer:", getTrgNum(i))
      break
  sys.exit(0)

if __name__ == "__main__":
  sys.exit(main())

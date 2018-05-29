
'''
Smallest multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

link: https://projecteuler.net/problem=5

'''

from __future__ import print_function
import sys
import numpy as np

def get_smallest(max_num):
  even_divl = []
  while (max_num >= 2520):
    check = True
    for i in range (1, 20):
      check = check and (max_num % i == 0)
      if not (check):
        break
    if (check):
      even_divl.append(max_num)
      #print (max_num)  #debug
    max_num-=1
  return np.min(even_divl)
    
def main():
  max_num = 500000000
  print("Answer:", get_smallest(max_num))
  sys.exit(0)
    
if __name__ == "__main__":
  sys.exit(main())

#!/bin/python
'''
link: https://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''

from __future__ import print_function
import sys

def mult_sum(up_lim):
  my_sum = 0
  for i in range(1, up_lim):
    if (i % 3 == 0) or (i % 5 == 0):
      #print(i)
      my_sum += i
  return my_sum
  
def main():
  answ = mult_sum(1000)
  print("Answer: ", answ)
  sys.exit(0)
  

if __name__ == "__main__":
  sys.exit(main())

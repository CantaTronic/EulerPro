#!/bin/python

'''
Sum square difference

link: https://projecteuler.net/problem=6
'''

from __future__ import print_function
import math
import sys

def sum_of_sqr(num):
  my_sum = 0
  for i in range(num+1):
    my_sum += math.pow(i,2)
  return my_sum

def sqr_of_sum(num):
  my_sum = 0
  for i in range(num+1):
    my_sum += i
  return math.pow(my_sum,2)

def get_diff(num):
  return abs(sqr_of_sum(num) - sum_of_sqr(num))

if __name__ == "__main__":
  print ("Answer: ", int(get_diff(100)))
  sys.exit(0)

'''
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
'''

from __future__ import print_function
import sys
import numpy as np
from mpmath import *

def test_precision():
  #the correct meaning of 1/3 is 0.(3)
  
  #np.float64 - gives mantissa 16 maximum, 16-teen 3 after the .
  tmp = str(np.float64(1/3.0))
  print("float64 \t", tmp)
  
  #mpmath - provides big mantissa (50 and more), but only first 16teen are 3s.
  mp.dps = 20
  tmp1 = str(mpf(1/3.0))
  print("mpmath \t\t", tmp1)

def all_equal(inp_str):
  #if all numbers in the list are equal, the period lenght is 1
  res = True
  for i in range(1,len(inp_str)):
    res &= inp_str[i] == inp_str[i-1]
  return res
  
def all_diff(inp_str):
    #if all digits are different, we have two probabilities:
    #1. the period is longer than 16 (anyway we can't catch it)
    #2. there is no period here
  
  
def period(inp_str):
  seq=inp_str[0]
  print("cur seq: ", seq)
  #if seq[1] !=
  return False
  

def main():
  #all_equal("111")
  print("111", all_equal("111")) #True
  print("123", all_equal("123")) #False
  print("1212", all_equal("1212")) #True
  

if __name__ == "__main__":
  sys.exit(main())

# -*- coding: utf-8 -*- 

'''
Largest palindrome product

link: https://projecteuler.net/problem=4

'''

from __future__ import print_function
import sys
import numpy as np
  
def is_palindrome(s):
  l = len(s)
  for i in range(l//2):
    if (s[i] != s[-1-i]):
      return False
  return True

def get_pal_prod(maxnum, bot_lim):
  pals = []
  for i in range(maxnum, bot_lim, -1):
    for j in range (maxnum, bot_lim, -1):
      #перемножаем два числа
      prod = i*j
      if is_palindrome(str(i*j)):
        pals.append(prod)
        break
  return np.max(pals)
    
def main():
  maxnum = 999
  bottom_limit = 900  #reasonable euristic
  print("Answer: ", get_pal_prod(maxnum, bottom_limit))
  sys.exit(0)
    
if __name__ == "__main__":
  sys.exit(main())

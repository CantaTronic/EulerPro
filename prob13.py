
'''
The task is to print out 10 first digits in a sum of 1050 digits.
https://projecteuler.net/problem=13

'''

from __future__ import print_function
import sys
import numpy as np

def main():
  f = open("bigNumber13.txt")
  bigSum = 0
  for line in f:
    bigSum = bigSum + int(line.rstrip())       #remove eol simbol out of line
  f.close()
  print(str(bigSum)[:10])
  sys.exit(0)
  
if __name__ == "__main__":
  sys.exit(main())

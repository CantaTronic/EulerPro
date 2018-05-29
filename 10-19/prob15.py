#!/usr/bin/python3

from __future__ import print_function
import math
import sys
from scipy.special import comb
#import scipy

def movNum(grSize):
  print(comb(2*grSize, grSize, exact=True))

if __name__ == "__main__":
  movNum(20);
  #print(math.factorial(5))
  #print(comb(2*n, 2, exact=True))


from __future__ import print_function
import sys
import numpy as np
 
def test():
  my_matr = readMatr(4, "my_test_matr.txt")
  print (my_matr)
  
def readMatr(matrSize, fname):
  #read diagonal matr of size matrSize from file fname into memory
  a = np.zeros((matrSize, matrSize))
  f = open(fname)
  it = 0
  for line in f:
    tmp = [int(s) for s in line.rstrip().split(' ')]      #break the line into list
    for j in range(it+1):
      a[it][j] = tmp[j]
    it = it + 1
  f.close()
  return a

def main():
  test()

if __name__ == "__main__":
  sys.exit(main())

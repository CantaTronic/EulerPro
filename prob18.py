
from __future__ import print_function
import sys
import numpy as np

def alg(mSize, fname):
  #walk around the tree
  my_matr = readMatr(mSize, fname)
  for i in range((mSize - 1),-1,-1):
    for j in range(i):
      sum1 = my_matr[i-1][j] + my_matr[i][j]
      sum2 = my_matr[i-1][j] + my_matr[i][j+1]
      my_matr[i-1][j] = max(sum1, sum2)
  return my_matr[0][0]
 
def test():
  print("test = ", alg(4, "my_test_matr18.txt"))
  
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
  #test()
  print("result = ", alg(15, "my_matr18.txt"))

if __name__ == "__main__":
  sys.exit(main())

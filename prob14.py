
from __future__ import print_function
import sys

'''
See the full condition at https://projecteuler.net/problem=14 

#n → n/2 (n is even)
#n → 3n + 1 (n is odd)

'''

def isOdd(num):
  return bool(num%2)

def getNewNum(n):
  count = 1
  while (n!=1):
    if (isOdd(n)):
      n = 3*n + 1
    else:
      n = n/2
    count = count + 1
  return count
  

def main():
  #test work
  max = 0
  my_num = 0
  for i in range (1,1000001):
    tmp = getNewNum(i)
    if (tmp > max):
      max = tmp
      my_num = i
  print("num = ", my_num, "\titer = ", max)
  #print(getNewNum(1000000))
  sys.exit(0)

if __name__ == "__main__":
  sys.exit(main())

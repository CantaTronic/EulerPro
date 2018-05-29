
'''
Even Fibonacci numbers

link: https://projecteuler.net/problem=2

'''

from __future__ import print_function
import sys

def get_even_Fibs_sum(limit):
    a = 1
    b = 1
    #print(a)   #debug
    sum_even = 0
    while (True):
      tmp = b
      b = a+b
      if (b >= limit):
        break;
      if (b % 2 == 0):
        sum_even += b
      a = tmp
      #print(b)   #debug
    return sum_even
  

def main():
    answ = get_even_Fibs_sum(4000000)
    print("sum is ", answ)
    sys.exit(0)

if __name__ == "__main__":
    sys.exit(main())

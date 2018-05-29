#!/bin/python

'''
10 001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?

link: https://projecteuler.net/problem=7
'''
from __future__ import print_function
import sys

def check_prime(num):
  for j in range(2, num):
    if (num % j == 0):
      return False
  return True

def get_Nst_prime(up_lim):
  count = 0 #primes counter
  i = 2 #the first prime
  while (count<up_lim):
    if check_prime(i):
      count += 1
      #print ("#",count,"\t",i)   #debug
    i+=1
  return i-1
    
def main():
  big_number = 10001
  print("Answer: ", get_Nst_prime(big_number))
  sys.exit(0)
    
if __name__ == "__main__":
  sys.exit(main())
  

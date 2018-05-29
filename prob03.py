
'''
The largest prime factor

link: https://projecteuler.net/problem=3
'''
from __future__ import print_function
import sys

def get_largest_prime(my_number):
  prime_fact = 1
  while (True):
    if (my_number % prime_fact == 0):
      #print(prime_fact)    #debug
      my_number /= prime_fact
    if (my_number == 1):
      break
    prime_fact+=1
  return prime_fact
  
def main():
  #my_number = 13195    #test
  my_number = 600851475143
  answ = get_largest_prime(my_number)
  print("Answer: ", answ)
  sys.exit(0)
  
    
if __name__ == "__main__":
  sys.exit(main())

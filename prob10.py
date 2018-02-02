
from __future__ import print_function
import sys
from math import sqrt, ceil
import numpy as np

'''
The task is to find the sum of all the primes below two million.

'''

def rwh_primes1(n):
    """ 
    Prime numbers generator taken from the https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    Returns  a list of primes < n """
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]] 
  
def main(argv=None):
    print(rwh_primes1(10))
    res = np.array(rwh_primes1(2000000)).sum()
    print ("Result = ", res)
    sys.exit(0)

if __name__ == "__main__":
    sys.exit(main())

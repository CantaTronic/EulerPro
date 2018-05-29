
from __future__ import print_function
import sys
import numpy as np

'''
See task description at https://projecteuler.net/problem=16
'''

if __name__ == "__main__":
    numb = str(pow(2,1000))
    this_sum = np.array([int(d) for d in numb]).sum()
    print (this_sum) 
    sys.exit(0)


from __future__ import print_function
import sys

def fibonacci():
    """Fibonacci numbers generator"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def main():  
  f = fibonacci()
  counter = -1
  for x in f:
    dig = len(str(x))
    #print (x, "\t", dig) 
    counter += 1
    if (dig > 999): 
      print("Result = ", counter, "number = ", x)
      break 
  print()
  sys.exit(0)

if __name__ == "__main__":
  sys.exit(main())

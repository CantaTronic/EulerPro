
from __future__ import print_function
import sys

def cleanStr(line):
  #return lenght of a clean string without spaces and dash
  return len(line.replace(" ",'').replace('-',''))

def countLetters(my_dict):
  my_sum = 0
  for i in range(1, len(my_dict)+1):
    my_sum = my_sum + cleanStr(my_dict[i])
  return my_sum

def test():
  print(cleanStr("three hundred and forty-two"))
  print(cleanStr("one hundred and fifteen"))
  my_dict = {1: 'one', 2: 'two', 3: 'three', 4:'four', 5:'five'}
  print(countLetters(my_dict))
  pass

def main():
    my_dict = {1: 'one', 2: 'two', 3: 'three', 4:'four', 5:'five'}
    sys.exit(0)

if __name__ == "__main__":
  test()
  sys.exit(main())

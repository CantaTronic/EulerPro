
from __future__ import print_function
import sys
import numpy as np

alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def getNameList(filename):
  f = open(filename)
  for line in f:
    line = line.replace("\"", "")
    nameList = line.split(',')
  f.close()
  return nameList

#for ch in alph:
## Get the ASCII number of a character
  #number = ord(ch) - ord('A') + 1
  #print(number)

# Get the character given by an ASCII number
#char = chr(number)

def main():
  nameList = getNameList("p022_names.txt")
  #print(len(nameList))
  #for i in range(15):
    #print(nameList[i])
  sys.exit(0)

if __name__ == "__main__":
  sys.exit(main())

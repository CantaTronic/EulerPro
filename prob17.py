
from __future__ import print_function
import sys

def nameGen(num):
  #take the number and generate it's name in English
  my_dict = {1: 'one', 2: 'two', 3: 'three', 4:'four', 5:'five', 
            6: 'six', 7:'seven', 8: 'eight', 9: 'nine', 10: 'ten',
            11: 'eleven', 12: 'twelve', 13: 'thirteen', 14:'fourteen', 15:'fifteen',
            16: 'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty',
            30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty',
            90: 'ninety', 100: 'hundred', 1000: 'one thousand'}
  if (num in my_dict):
    return my_dict[num]
  if (num<100):
    fisrtDig = 10*(num/10)
    secDig = num - fisrtDig
    numName = my_dict[fisrtDig]+'-'+my_dict[secDig]
    return numName

  

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
    #my_dict = {1: 'one', 2: 'two', 3: 'three', 4:'four', 5:'five', 
               #6: 'six', 7:'seven', 8: 'eight', 9: 'nine', 10: 'ten',
               #11: 'eleven', 12: 'twelve', 13: 'thirteen', 14:'fourteen', 15:'fifteen',
               #16: 'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty'}
    for i in range(1,101):
        print(nameGen(i))
    #print(nameGen(19))
    #print(nameGen(29))
    #print(nameGen(63))
    #print(nameGen(14))
    #print(nameGen(88))
    sys.exit(0)

if __name__ == "__main__":
  #test()
  sys.exit(main())

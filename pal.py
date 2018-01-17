# -*- coding: utf-8 -*- 

'''
по нисходящей с 999 до 0 
  перемножаем 2 числа.
  проверяем, палиндром ли получился.
  если да, выходим из цикла
  '''
  
def is_palindrome(s):
  l = len(s)
  for i in range(l//2):
    if (s[i] != s[-1-i]):
      return False
  return True

  
maxnum = 999
for i in range(maxnum, 900, -1):
  for j in range (maxnum, 900, -1):
    #перемножаем два числа
    prod = i*j
    if is_palindrome(str(i*j)):
      print "pal", prod
      break
  #if (flag):
    #break

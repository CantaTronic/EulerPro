#!/bin/python3
#-*- coding: utf-8 -*-

'''
Perfect number:
sum(all_divisors(Num)) = Num
1 + 2 + 4 + 7 + 14 = 28

Deficient number:
sum(all_divisors(Num)) < Num

Abundant number:
sum(all_divisors(Num)) > Num

12 - the smallest abundant number.
12 + 12 = 24 - the smallest num can be written as a sum of two abundats nums.

All x > 28123 can be written as the sum of two abundant numbers. 

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

Самый очевидный алгоритм:
  - Найти все Abundant числа до 28123, сохранить в список
  - Для каждого числа i от 0 до 28123 перебирать сумму всевозможных пар чисел меньше числа i
  - если ни одна сумма не соспала с числом, добавляем число в массив

'''



#for i in range(10, 0, -1):
  #print(i)
  
import math
import numpy as np
#from _future_ import print_function
  
def prop_divisor(number):
  #return the list of proper divisors 
  a = []
  i = int(math.sqrt(number))
  while (i > 0):
    if (number % i == 0):
      a.append(i)
      a.append(number/i)
    i = i - 1
  return a[:-1]

def abundant(num):
  #check if number is abundant or not
  arr = np.array(prop_divisor(num))
  sum_div = np.array(prop_divisor(num)).sum()
  #print (num, '\t', arr, '\t', sum_div)
  return (sum_div >= num)


  
if __name__ == "__main__":
  #look for all abundant numbers
  upper_limit = 28123
  
  #stage 1: make list of all abundant numbers
  abn_num = []
  for num in range (10, upper_limit):
    #check if the number is abundant
    if (abundant(num)):
      #if it is, add it in the list
      abn_num.append(num)
      
  for num in abn_num:
    print(num)
    
  SRange = min(len(abn_num), upper_limit+1)
  res = []  #то, что мы хотим на выходе - массив чисел, непредставимых в виде суммы
  for i in range (1, upper_limit+1):
    Npred = True  #представимо личисло в виде сумму двух чисел их abn_num. по умолчанию - нет
    for j in range (SRange):
      for k in range (SRange):
        num_sum = abn_num[j]+abn_num[k]
        Npred &= not (num_sum == i)
        if (not Npred):  #если число представимо суммой
          break     #выходим из цикла
    if (Npred):
      res.append(i)
  print(res)
  
  print("sum: ", np.array(res).sum())
          
  #- если ни одна сумма не соспала с числом, добавляем число в массив

    
  #check if number can't be 

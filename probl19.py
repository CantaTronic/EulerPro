# -*- coding: utf-8 -*- 

from __future__ import print_function
import sys
import numpy as np

'''
How many Sundays fell on the first of the month 
during the twentieth century (1 Jan 1901 to 31 Dec 2000)? 
'''

'''
September, April, June and November have 30 days -> shift day + 2 in 7-days cicle
At leap years February make 1 day shift and zero shift in others
January, March, May, July, August, October, December have 31 -> 3-days shift
'''

def dayShift(day, month, year):
  if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
    day += 3
  if (month == 4 or month == 6 or month == 9 or month == 11 ):
    day += 2
  if (month == 2):
    if not (year % 4 != 0 or (year % 100 == 0 and year % 400 !=0)):
    #if leap year
      day += 1
  day = day % 7
  #Sunday is day 0
  return day

def getDayCount():
  FirstDay = 2  #tuesday
  startMonth = 1  #January
  startYear = 1901 #startYear
  countSund = 0
  print(" ===== ", startYear, " ===== ")
  print(startMonth, "'s first day", FirstDay)
  while (startYear < 2001):
    FirstDay = dayShift(FirstDay, startMonth, startYear)
    if (FirstDay == 0):
      countSund += 1
    startMonth += 1
    if (startMonth == 13):
      startMonth = 1
      startYear += 1
      print(" ===== ", startYear, " ===== ")
    print(startMonth, "'s first day", FirstDay)
  print ("I count ", countSund, " Sundays so far")
  

if __name__ == "__main__":
  getDayCount()

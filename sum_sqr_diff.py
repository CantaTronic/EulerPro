
import math

def sum_of_sqr(num):
  my_sum = 0
  for i in range(num+1):
    my_sum += math.pow(i,2)
  return my_sum


def sqr_of_sum(num):
  my_sum = 0
  for i in range(num+1):
    my_sum += i
  return math.pow(my_sum,2)

def get_diff(num):
  return abs(sqr_of_sum(num) - sum_of_sqr(num))

#print sum_of_sqr(10)
#print sqr_of_sum(10)
print "diff = ", get_diff(100)

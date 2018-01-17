
a = 1
b = 1
print a
sum_even = 0;
while (True):
  tmp = b
  b = a+b
  if (b >= 4000000):
    break;
  if (b % 2 == 0):
    sum_even += b
  a = tmp
  print b
print "sum is ", sum_even


#my_num = 2520

#def range_check(my_num, num):
  #check = True
  #for i in range (1, num):
    #check = check and (my_num % i == 0)
#print check


import sys

#my_num = sys.maxint
my_num = 500000000
while (True):
  check = True
  for i in range (1, 20):
    check = check and (my_num % i == 0)
    if not (check):
      break
  if (check):
    print my_num
  my_num-=1
  if (my_num < 2520):
    sys.exit(0)
    

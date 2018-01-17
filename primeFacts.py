
#import sys

#my_number1 = 13195
my_number = 600851475143
i = 1
while (True):
  if (my_number % i == 0):
    print i
    my_number /= i
  if (my_number == 1):
    break
  i+=1
    
#print sys.maxint > my_number

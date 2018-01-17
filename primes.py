
def check_prime(num):
  for j in range(2, num):
    if (num % j == 0):
      return False
  return True

my_num = 20
count = 0
i = 2
while (count<10001):
  if check_prime(i):
    count += 1
    print "#",count,"\t",i
  i+=1
  

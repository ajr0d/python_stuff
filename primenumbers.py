# Prints prime numbers from 3 to 100.  Don't forget what prime numbers are in future.

print("Prime numbers from 1 to 100 are:")
for num in range(1, 101):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)

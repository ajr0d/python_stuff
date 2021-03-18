# Basic fizzbuzz.  Remember the modulo operator which returns the remainder of dividing two numbers

for i in range(1, 101):
	if i % 3 == 0 and i % 5 == 0:
		print("FizzBuzz")
	elif i & 3 == 0:
		print("Fizz")
	elif i & 5 == 0:
		print("Buzz")
	else:
		print(i)	
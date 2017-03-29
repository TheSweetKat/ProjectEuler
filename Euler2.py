# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms

a, b = 0, 1
fib = []

while b < 4000000:
	a, b = b, a + b
	if(b % 2 == 0):
		fib.append(b)


c = sum(fib)
print(c)
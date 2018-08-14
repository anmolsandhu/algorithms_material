

dict = {}

def fib(n):
	if dict.get(n) != None:
		return dict[n]
	if n <= 1:
		return n
	else:
		f = fib(n-1) + fib(n-2)
		dict[n] = f
		return f


print fib(200)
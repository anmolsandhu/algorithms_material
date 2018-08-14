

def fib_rec(n):
	if n <= 1:
		return n
	else:
		return fib_rec(n-1) + fib_rec(n-2)


def panildrome_recursive(word, i, j):
	#print(" %d = word[%d]  and  %d = word[%d]".format(word[i], i, j, word[j]))
	if i == j:
		return True
	elif word[i] != word[j]:
		return False
	else:
		#print "hello"
		return True and panildrome_recursive(word, i + 1, j -1)

def fact_rec(n):
	if n <= 1:
		return 1
	else:
		return n*fact_rec(n-1)


def power_rec(num, pow):
	if pow == 1:
		return num
	else:
		return num * power_rec(num, pow - 1)

print fact_rec(8)
print panildrome_recursive('baceb', 0, 4)

print power_rec(4, 5)
print fib_rec(4)
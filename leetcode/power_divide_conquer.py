
results = {}


def power(x, n):
	global results
	print results
	if n == 2:
		return x * x
	elif n == 1:
		return x
	else:
		s = 0
		a = 0
		b = 0
		m = n / 2
		r = n - m
		if results.get(m) == None:
			a = power(x, m)
			results[m] = a
		else:
			a = results[m]

		if results.get(r) == None:
			b = power(x, r)
			results[r] = b
		else:
			b = results[r]

		if results.get(n) == None:
			s = a * b
			results[n] = s
		else:
			s = results[n]

		return s

print results
print power(2, 99876154289178123785657482187919898178732183718)
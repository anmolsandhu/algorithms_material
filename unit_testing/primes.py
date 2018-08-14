

def prime(number):

	for i in xrange(2, number):
		if number % i == 0:
			return False

	return True 


print prime(11)
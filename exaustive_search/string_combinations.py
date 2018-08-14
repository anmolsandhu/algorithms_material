

permutations = []
subset_permutations = []

def generate_string_combinations(current, leftover):
	global permutationsb
	global subset_permutations
	if len(leftover) == 0:
		print "final ----", current
		permutations.append(current)
		return
	else:
		subset_permutations.append(current)
		for i in range(0, len(leftover)):

			remaining = leftover[0:i] + leftover[i+1:]
			print current ,"  ",  leftover
			generate_string_combinations(current + leftover[i], remaining)


def string_combinations(arr):
	generate_string_combinations('', arr)



print string_combinations('abc')
print permutations

print subset_permutations + permutations
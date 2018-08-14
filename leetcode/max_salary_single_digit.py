

def not_oprimized(numbers):

	salary_numbers = []
	for i in range(len(numbers)):
		largest = pick_largest(numbers)
		salary_numbers.append(largest)

	return salary_numbers



def pick_largest(array):

	best_index = 0
	for i in range(len(array)):
		if array[i] > array[best_index]:
			best_index = i

	val = array[best_index] 
	array[best_index] = 0
	return val


def is_optimized(numbers):
	print numbers
	numbers.sort(reverse = True)
	return numbers



a = [1,9,2,0,1, 9, 4,5,9,8,5,9]
print not_oprimized(a)
a = [1,9,2,0,1, 9, 4,5,9,8,5,9]
print is_optimized(a)
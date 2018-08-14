

def cyclic_rotation(array):

	prev = 0

	x = array[len(array) - 1]

	prev = array[0]
	for i in range(1, len(array)):
		temp = array[i]
		array[i] = prev
		prev = temp

	array[0] = x

	return array

a = [1,2,3,4,5]
print cyclic_rotation(a)



def selection_sort(array):

	for i in range(len(array)):
		min_index = i
		for j in range(i, len(array)):
			if array[j] < array[min_index]:
				min_index = j
		swap(array, i, min_index)

	return array


def swap(array, i, j):

	temp = array[i]
	array[i] = array[j]
	array[j] = temp




a = [4,7,8,1,2,3,4,0,67,87,12]

print selection_sort(a)
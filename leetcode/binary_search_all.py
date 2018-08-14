



def Binary_Search(array, low, high, key):

	mid = 0
	low = low
	high = high

	while low <= high:
		mid = (low + high)/ 2
		if array[mid] == key:
			return mid
		elif array[mid] < key:
			low = mid + 1
		else:
			high = mid - 1

	return mid


def Binary_search_recursive(array, low, high, key):
	if low > high:
		return - 1
	mid = (low + high) / 2
	if array[mid] == key:
		return mid
	elif array[mid] < key:
		Binary_search_recursive(array, mid + 1, high, key)
	else:
		Binary_search_recursive(array, low, mid + 1, key)


def wrapper_function(array, low, high, queries):

	indexes = []
	for i in range(len(queries)):
		indexes.append(Binary_Search(array, low, high, queries[i]))

	return indexes




a = [1, 4, 7,9,12,16,19,23,43, 90]
print len(a)
print Binary_Search(a, 0, len(a) -1, 1)
print Binary_Search(a, 0, len(a) - 1, 1)

# b = [1, 5, 8, 12, 13]
# que = [8, 1, 23, 1, 11]
# print wrapper_function(b, 0, len(que) -1, que)
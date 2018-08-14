


import random


def quick_sort(arr, l, r):
	if l >= r:
		return
	else:
		k = random.randrange(l, r, 1)
		temp = arr[l]
		arr[l] = arr[k]
		arr[k] = temp
		m1, m2 = partition(arr, l, r)
		print " m1: ", m1, " m2: ", m2
		quick_sort(arr, m2 + 1, r)
		quick_sort(arr, l, m1 - 1)



def partition(arr, l, r):
	x = arr[l]
	j = l
	k = 0
	for i in range(l+1, r+1):
		if x >= arr[i]:

			j = j + 1
			temp = arr[i]
			arr[i] = arr[j]
			arr[j] = temp


	temp = arr[l]
	arr[l] = arr[j]
	arr[j] = temp

	for i in range(l , r+ 1):
		if arr[i] == x:
			k = i
			break

	return [k, j]


a = [7, 14, 3, 12, 9, 11, 7, 2, 7]
quick_sort(a, 0, len(a) - 1)
print a
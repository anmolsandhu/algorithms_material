import random


def quick_sort(arr, l, r):
	if l >= r:
		return
	else:
		k = random.randrange(l, r, 1)
		temp = arr[l]
		arr[l] = arr[k]
		arr[k] = temp
		m = partition(arr, l, r)
		quick_sort(arr, m + 1, r)
		quick_sort(arr, l, m - 1)



def partition(arr, l, r):
	x = arr[l]
	j = l
	for i in range(l+1, r+1):
		if x > arr[i]:
			j = j + 1
			temp = arr[i]
			arr[i] = arr[j]
			arr[j] = temp


	temp = arr[l]
	arr[l] = arr[j]
	arr[j] = temp

	return j


a = [7, 14, 3, 12, 9, 11, 6, 2, 0]
quick_sort(a, 0, len(a) - 1)
print a
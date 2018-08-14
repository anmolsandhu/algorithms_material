

total_inversion = 0


def merge_sort(array):
	if len(array) > 1:
		mid = len(array) / 2
		a = merge_sort(array[:mid])
		b = merge_sort(array[mid:])
		s = Merge(a, b)
		print "sorted", s
		return s
	else:
		return array



def Merge(a, b):
	#inversions = 0
	print "merging ", a, " ", b
	d = []

	i = 0
	j = 0

	while i < len(a) and j < len(b):

		if a[i] <= b[j]:
			d.append(a[i])
			i = i+ 1
		else:
			#inversions += 1
			d.append(b[j])
			j = j + 1

	print "merge result before",  d
	if i == len(a):
		for k in range(j, len(b)):
			d.append(b[k])
			#inversions += 1
	elif j == len(b):
		for k in range(i, len(a)):
			d.append(a[k])

	# global total_inversion 
	# total_inversion += inversions
	return d

g = [14, 7, 3, 12, 9, 11, 6, 2]
print merge_sort(g)
#print total_inversion

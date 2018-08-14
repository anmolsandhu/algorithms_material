

def large_small(array):

	max_no = float("-inf")
	min_no = float("inf")
	for i in array:
		if i > max_no:
			max_no = i
		if i < min_no:
			min_no = i

	print max_no
	print min_no

a = [1,2,3,4,5,-1,3,4,-5,-789,98,-78,99,-67]
large_small(a)
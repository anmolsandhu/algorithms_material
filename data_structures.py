


def reverse_array(a, start_point):
	if len(a) == start_point:
		return
	else:
		reverse_array(a, start_point + 1)
		print a[start_point]


a = [4,3,2,1]

reverse_array(a, 0)
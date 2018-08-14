


a = [[3,8], [5, 6], [7, 8], [10, 12], [10,14], [11, 16]]




def collect_signatures(arr):
	ar = arr
	j = 0
	k = 0
	i = 0
	flag = True

	point = []
	while(flag):

		lowest_highest_val = ar[i]
		next_high_val = ar[i + 1]

		if lowest_highest_val[1] >= next_high_val[0] and ar[k][1] >= next_high_val[0]:
			j += 1
			i += 1
		else:
			point.append(ar[j][0])
			i += 1
			k = i
			j = i

		if(i >= len(ar) - 1):
			flag = False
			point.append(ar[j][0])
			#print i, "flag"
		
	print point

def get_point(aa, k, j):
	for i in range(k, j+1):
		print aa[i]

	print "list"


collect_signatures(a)


def max_prizes(n):

	points = []
	if n <= 2:
		return points.append(n)

	sum_of_prizes = 0
	for i in range(1, n+1):

		total_sum = sum_of_prizes + i
		if total_sum == n:
			points.append(i)
		elif n - total_sum > i:
			points.append(i)
			sum_of_prizes += i
		
	return len(points)


print max_prizes(182414564)
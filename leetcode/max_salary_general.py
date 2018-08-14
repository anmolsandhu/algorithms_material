

def general_Case_salary(numbers):


	best_case = pick_best(numbers)





def pick_best(numbers):

	best_index = 0
	for i in range(len(numbers)):
		best_index_len = len(numbers[best_index])
		current_len = len(numbers[i])

		anm = min(best_index_len, current_len)

		for j in range(anm):
			if int(numbers[i][j]) > (best_index[i][j])
				


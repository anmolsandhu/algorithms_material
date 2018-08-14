

positions = [ [0 for i in range(8)] for j in range(8)]

#print_matrix(positions)
def print_matrix(matrix):
	for i in matrix:
		print i

def add_matrix_element(i, j, matrix, element):
	matrix[i][j] = element


def place_queens(k, positions):

	if k > 7:
		print print_matrix(positions)
		return True

	for i in range(k, 8):
		for j in range(0, 8):
			can_put_val = check_validity(i, j)
			if can_put_val:
				positions[j][i] = 1
				print_matrix(positions)
				val = place_queens(i + 1, positions)
				if val == False:
					positions[j][i] = 0
				else:
					return True
		
		return False


def check_validity(column, row):

	print "check_validity ",  column, "   ", row

	for i in range(8):
		if positions[row][i] == 1:
			return False

	for i in range(8):
		if positions[i][column] == 1:
			return False

	row_ = row
	column_ = column


	loop_flag = True
	while loop_flag:
		if row_ > -1 and column_ > -1:
			if positions[row_][column_] == 1:
				return False
		else:
			loop_flag = False

		row_ = row_ - 1
		column_ = column_ - 1

	row_ = row
	column_ = column


	loop_flag = True
	while loop_flag:
		if row_ < 8 and column_ > -1:
			if positions[row_][column_] == 1:
				return False
		else:
			loop_flag = False

		row_ = row_ + 1
		column_ = column_ - 1


	print "approved  "
	return True


place_queens( 0, positions)
print_matrix(positions)





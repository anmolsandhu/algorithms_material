


positions = [ [0 for i in range(8)] for j in range(8)]

#print_matrix(positions)
def print_matrix(matrix):
	for i in matrix:
		print i

def add_matrix_element(i, j, matrix, element):
	matrix[i][j] = element


def place_queens(i, j):
	if i > 7:
		print_matrix(positions)
		return True

	for k in range(i, j):
		for l in range(0, 8):
			can_place = check_placement( k, l)
			if can_place:
				print "approved " , k, "  ", l 
				positions[k][l] = 1
				val = place_queens(k + 1, j)
				if val == False:
					positions[k][l] == 0
				else:

		return False


	return False


def check_placement( row, column):
	print "check_placement ", row, " ", column
	flag = True

	for i in range(8):
		if positions[row][i] == 1:
			if column == i:
				pass
			else:
				return False

	for i in range(8):
		if positions[i][column] == 1:
			if row == i:
				pass
			else:
				return False




	loop_flag = True
	k = row -1
	l = column - 1
	while loop_flag:
		if k < 0 or j < 0:
			loop_flag = False			
		else:
			if positions[k][l] != 0:
				return False

		k = k - 1
		l = l - 1

	loop_flag = True
	k = row + 1
	l = column - 1
	while loop_flag:
		if k < 8 and l > -1:
			if positions[k][l] != 0:
				return False
		else:
			loop_flag = False

		k = k + 1
		l = l - 1

	return True



#print_matrix(positions)	
# add_matrix_element(0, 0, positions, 1)
# add_matrix_element(5, 5, positions, 1)
# print_matrix(positions)
# print check_placement(5,4)

#print_matrix(positions)
place_queens(0, 8)
print "final"
print_matrix(positions)

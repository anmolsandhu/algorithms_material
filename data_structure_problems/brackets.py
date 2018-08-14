


def bracket_check(bracket_array):

	stack = []

	brackets_opening = ['(', '[', '{']
	brackets_closing = [')', ']', '}']

	for bracket in range(len(bracket_array)):

		if bracket in brackets_opening:
			stack.append(bracket)
		elif bracket in brackets_closing:
			index = brackets_closing.index(bracket):
			if index == 0 and stack[len(stack) - 1] == brackets_opening[0]:
				stack.pop()
			elif index == 1 and stack[len(stack) - 1] == brackets_opening[1]:
				stack.pop()
			elif index == 2 and stack[len(stack) - 1] == brackets_opening[2]:
				stack.pop()
			else:
				return False

	return True

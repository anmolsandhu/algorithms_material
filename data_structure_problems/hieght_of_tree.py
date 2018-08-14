



class Node():

	def  __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


def hieght_of_tree(node):
	if node == None:
		return 0
	else:
		left = hieght_of_tree(node.left) + 1
		right = hieght_of_tree(node.right) + 1

		if left > right:
			return left
		else:
			return right

a = Node
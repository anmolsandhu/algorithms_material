


class Node():

	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


def find(node, element):
	if node.data == element:
		return node
	elif node.data > element:
		if node.left != None:
			return find(node.left, element)
		return node
	elif node.data < element:
		if node.right != None:
			return find(node.right, element)
		return node

def insert_element(node, element):
	#print node.data, "  ", element
	if node.data > element:
		if node.left == None:
			node.left = Node(element)
		else:
			insert_element(node.left, element)
	elif node.data < element:
		if node.right == None:
			node.right = Node(element)
		else:
			insert_element(node.right, element)
	else:
		pass

def inorder(node):
	if node != None:
		inorder(node.left)
		print node.data
		inorder(node.right)

# this will find the min node in the given subtree
def find_min_node(node):
	if node == None:
		return None

	current_node = node
	while current_node.left != None:
		current_node = current_node.left

	return current_node

def find_inorder_successor(node, max_node, element):


	max_node_successor = max_node

	if node.data == element:
		if node.right != None:
			return find_min_node(node.right)
		else:
			return max_node_successor 
	elif node.data > element:
		max_node_successor = node
		return find_inorder_successor(node.left, max_node_successor, element)
	elif node.data < element:
		return find_inorder_successor(node.right, max_node_successor, element)

def find_range(node, element1, element2):
	elements = []
	root = node
	
	current_node = find(root , element1)
	while current_node.data <= element2:
		print current_node.data
		if current_node.data >= element1:
			elements.append(current_node)

		current_node = find_inorder_successor(root, None, current_node.data)
		if current_node == None:
			break

	return elements 


	







a = Node(20)
insert_element(a, 22)
insert_element(a, 8)
insert_element(a, 4)
insert_element(a, 12)
insert_element(a, 10)
insert_element(a, 14)
print find_range(a, 7, 18)
#print find_inorder_successor(a, None, 4).data
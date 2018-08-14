

class Node():

	def __init__(self, data_a):
		self.data = data_a
		self.left = None
		self.right = None


queue = []

def inorder(node):
	if node == None:
		return 
	else:
		inorder(node.left)
		print node.data
		inorder(node.right)


def preorder(node):
	if node == None:
		return
	else:
		print node.data
		preorder(node.left)
		preorder(node.right)


def postorder(node):
	if node == None:
		return
	else:
		postorder(node.left)
		postorder(node.right)
		print node.data

def level_order(node):



a = Node(1)
a.left = Node(2)
a.left.left = Node(4)
a.left.right = Node(5)
a.right = Node(3)

inorder(a)
print 'preorder'
preorder(a)
print 'postorder'
postorder(a)
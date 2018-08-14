import time


class Node:

	def __init__(self, key):
		self.key = key
		self.next = None

class AdjacencyList:

	def __init__(self):
		self.head = None
		self.next = None


class Graph:

	def __init__(self):
		self.vertexes = None

	def addVertex(self, key):
		if self.vertexes == None:
			self.add_vertex_to_head(key)
		else:
			current = self.vertexes
			
			#print "doing ", current.head.key, "  ",  key
			if current.head.key == key:
					#print "ok"
					return
			while current.next != None:
				if current.head.key == key:
					#print "ok"
					return
				else:
					current = current.next

			if current.head.key ==  key:
				return

			new_adjacency_list = AdjacencyList()
			new_node = Node(key)
			new_adjacency_list.head = new_node
			current.next = new_adjacency_list


	def add_vertex_to_head(self, key):
		#print "head, ", key
		new_adjacency_list = AdjacencyList()
		new_node = Node(key)
		new_adjacency_list.head = new_node
		self.vertexes = new_adjacency_list

	def add_edge(self, frm, t):
		self.addVertex(frm)
		self.addVertex(t)

		current = self.vertexes
		while current.head.key != frm:
			current = current.next

		current_node = current.head

		while current_node.next != None:
			if current_node.key == t:
				return
			else:
				current_node = current_node.next

		if current_node.key == t:
				return
		else:
			new_node_1 = Node(t)
			current_node.next = new_node_1

		#self.add_edge(t, frm)

	def __str__(self):
		vertices = []

		current = self.vertexes

		while current != None:
			vertices.append(current.head.key)
			current = current.next

		return str(vertices)

	def get_neighbours(self, key):

		current = self.vertexes

		while current != None:
			if current.head.key == key:
				vertices = []
				current_node = current.head.next
				while current_node != None:
					vertices.append(current_node.key)
					current_node = current_node.next

				return vertices

			current = current.next

		return None

	def print_vertexes(self):
		adjacency_list = self.vertexes
		while adjacency_list != None:
			print " vertex",adjacency_list.head.key, " neigbours  ", self.get_neighbours(adjacency_list.head.key) 
			adjacency_list = adjacency_list.next

def _explore(node, graph, visited):
	if node == None:
		return
	time.sleep(4)
	print node.key , " key   ", visited, " next node " ,  node.next
	visited[node] = 1

	while node != None:
		if visited.get(node) == None:
			_explore(get_node_with_key(node.next, g), g, visited)

		node = node.next


def get_node_with_key(node, graph):
	if node == None:
		return None
	key = node.key

	adjacency_list = graph.vertexes
	while adjacency_list != None:

		if adjacency_list.head.key != key:
			return adjacency_list.head.next

		adjacency_list = adjacency_list.next

	return adjacency_list.head.next



def explore(node, graph):
	visited = {}

	_explore(node, graph, visited)

	return visited


g = Graph()
g.addVertex(2)
g.add_edge(2, 5)
g.add_edge(3, 4)
g.add_edge(3, 5)
g.add_edge(3, 6)
g.add_edge(2, 3)
print g.get_neighbours(5)
print g.get_neighbours(3)
print g

print g.vertexes.head.key
g.print_vertexes()
print explore(g.vertexes.head.next.next , g)



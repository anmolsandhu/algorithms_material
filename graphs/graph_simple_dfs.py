


graph = { "a" : ["c"],
		  "b" : ["c", "e"],
		  "c" : ["a", "b", "d", "e"],
		  "d" : ["c"],
		  "e" : ["c", "b"],
		  "f" : []
		}

#explore the whole connected componetnts of the node 

def explore(node, visited, g, cc):

	visited[node] = cc

	for node_next in g[node]:
		if node_next not in visited:
			explore(node_next, visited, g, cc)


#explore the whole graph
def dfs(graph):
	visited = {}
	cc = 0
	for node in graph:
		if node not in visited:
			explore(node, visited, graph, cc)
			cc += 1
	return visited

# def explore_for_undirected(node, visited, g):
# 	visited[node] = 1

# 	for node_next in g[node]:


print dfs(graph)
from collections import deque
from heapq import heappush, heappop


def shortest_shortest_path(graph, source):
	"""
	Params: 
	  graph.....a graph represented as a dict where each key is a vertex
				and the value is a set of (vertex, weight) tuples (as in the test case)
	  source....the source node
	  
	Returns:
	  a dict where each key is a vertex and the value is a tuple of
	  (shortest path weight, shortest path number of edges). See test case for example.
	"""

	### TODO
	def help(visit, front):
		if len(front) == 0:
			return visit

		else:

			distance_weight, distance_edges, node = heappop(front)
			if node not in visit:

				visit[node] = (distance_weight, distance_edges)

				for neighbor, weight in graph[node]:
					heappush(front, (distance_weight + weight, distance_edges + 1, neighbor))
				return help(visit, front)

			else:
				return help(visit, front)

	visit = dict()
	front = []
	heappush(front, (0, 0, source))

	return help(visit, front)


def test_shortest_shortest_path():

	graph = {
	 's': {('a', 1), ('c', 4)},
	 'a': {('b', 2)},  # 'a': {'b'},
	 'b': {('c', 1), ('d', 4)},
	 'c': {('d', 3)},
	 'd': {},
	 'e': {('d', 0)}
	}
	result = shortest_shortest_path(graph, 's')
	# result has both the weight and number of edges in the shortest shortest path
	assert result['s'] == (0, 0)
	assert result['a'] == (1, 1)
	assert result['b'] == (3, 2)
	assert result['c'] == (4, 1)
	assert result['d'] == (7, 2)


def bfs_path(graph, source):
	"""
	Returns:
	  a dict where each key is a vertex and the value is the parent of 
	  that vertex in the shortest path tree.
	"""

	###TODO
	def help_sec(visit, front, parent):
		if len(front) == 0:
			return parent

		else:
			node = front.popleft()
			visit.add(node)
			for n in graph[node]:
				if n not in front and n not in visit:
					parent[n] = node
					front.append(n)
			return help_sec(visit, front, parent)

	front = deque()
	front.append(source)

	parent = dict()
	visit = set()

	return help_sec(visit, front, parent)


def get_sample_graph():
	return {'s': {'a', 'b'}, 'a': {'b'}, 'b': {'c'}, 'c': {'a', 'd'}, 'd': {}}


def test_bfs_path():
	graph = get_sample_graph()
	parents = bfs_path(graph, 's')
	assert parents['a'] == 's'
	assert parents['b'] == 's'
	assert parents['c'] == 'b'
	assert parents['d'] == 'c'


def get_path(parents, destination):
	"""
	Returns:
	  The shortest path from the source node to this destination node 
	  (excluding the destination node itself). See test_get_path for an example.
	"""
	###TODO
	if destination not in parents:
		return ""

	else:
		return get_path(parents, parents[destination]) + parents[destination]


def test_get_path():
	graph = get_sample_graph()
	parents = bfs_path(graph, 's')
	assert get_path(parents, 'd') == 'sbc'

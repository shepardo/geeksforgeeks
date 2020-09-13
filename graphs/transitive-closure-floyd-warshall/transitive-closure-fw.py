# Python program for transitive closure using Floyd Warshall Algorithm
#Complexity : O(V^3)

from collections import defaultdict

#Class to represent a graph
class Graph:

	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[0 for j in range(vertices)] for i in range(vertices)]

	# A utility function to print the solution
	def printSolution(self, reach):
		print ("Following matrix transitive closure of the given graph ")
		for i in range(self.V):
			for j in range(self.V):
				print( "%7d\t" %(reach[i][j]), end='')
			print("")


	# Prints transitive closure of graph[][] using Floyd Warshall algorithm
	def transitiveClosure(self,graph):
		'''reach[][] will be the output matrix that will finally
		have reachability values.
		Initialize the solution matrix same as input graph matrix'''
		reach =[i[:] for i in graph]
		'''Add all vertices one by one to the set of intermediate
		vertices.
		---> Before start of a iteration, we have reachability value
		for all pairs of vertices such that the reachability values
		consider only the vertices in set
		{0, 1, 2, .. k-1} as intermediate vertices.
		----> After the end of an iteration, vertex no. k is
		added to the set of intermediate vertices and the
		set becomes {0, 1, 2, .. k}'''
		for k in range(self.V):

			# Pick all vertices as source one by one
			for i in range(self.V):

				# Pick all vertices as destination for the
				# above picked source
				for j in range(self.V):

					# If vertex k is on a path from i to j,
					# then make sure that the value of reach[i][j] is 1
					reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])

		self.printSolution(reach)

	def init_from_external_graph(self, graph):
		self.graph = graph

	def get_graph(self):
		return self.graph

	def add_edge(self, u, v):
		self.graph[u][v] = 1


if __name__ == '__main__':
	'''
	g= Graph(4)
	graph = [[1, 1, 0, 1],
			[0, 1, 1, 0],
			[0, 0, 1, 1],
			[0, 0, 0, 1]]
	'''
	v = int(input())
	e = int(input())
	g = Graph(v)
	while e > 0:
		u, v = map(int, input().split(' '))
		g.add_edge(u, v)
		e -= 1

	# The Floyd-Warshall needs self links for all nodes
	for i in range(v):
		g.add_edge(i, i)

	graph = g.get_graph()

	#Print the solution
	g.transitiveClosure(graph)

#This code is contributed by Neelam Yadav

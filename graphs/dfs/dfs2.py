# Python3 program to print DFS traversal
# from a given given graph
from collections import defaultdict

# This class represents a directed graph using
# adjacency list representation
class Graph:

	# Constructor
	def __init__(self, n):

		self.n = n
		# default dictionary to store graph
		self.graph = defaultdict(list)

	# function to add an edge to graph
	def addEdge(self, u, v):
		self.graph[u].append(v)

	# A function used by DFS
	def DFSUtil(self, v, visited):

		# Mark the current node as visited
		# and print it
		visited[v] = True
		print(v, end = ' ')

		# Recur for all the vertices
		# adjacent to this vertex
		for i in self.graph[v]:
			#print('i equals {0}'.format(i))
			if visited[i] == False:
				self.DFSUtil(i, visited)

	# The function to do DFS traversal. It uses
	# recursive DFSUtil()
	def DFS(self, v):

		#print('max(self.graph): {0}'.format(max(self.graph)))
		# Mark all the vertices as not visited
		#visited = [False] * (max(self.graph)+1)
		visited = [False] * self.n

		# Call the recursive helper function
		# to print DFS traversal
		self.DFSUtil(v, visited)

# Driver code

# Create a graph given
# in the above diagram
if __name__ == '__main__':
  n = int(input())
  e = int(input())
  g = Graph(n)
  start_node = int(input())
  while e > 0:
    line = input()
    data = line.split(' ')
    g.addEdge(int(data[0]), int(data[1]))
    e -= 1

#print("Following is DFS from (starting from vertex 2)")
  g.DFS(start_node)

# This code is contributed by Neelam Yadav

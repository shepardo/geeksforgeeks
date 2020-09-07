# Finding mother vertex directed graph in python
# See https://www.geeksforgeeks.org/find-a-mother-vertex-in-a-graph/
# This implementation uses BFS & matrix representation

from array import *

class Graph():
    def __init__(self, V):
        self.V = V
        self.nodes = [];
        for i in range(V):
            self.nodes.insert(0, [0] * V)

    def add_edge(self, v, u):
        self.nodes[v][u] = 1

    def find_mother_vertex(self):
        for i in range(self.V):
            if self.is_mother_vertex(i):
                return i
        return -1

    def is_mother_vertex(self, starter_node):
        # TODO:
        V = self.V
        visited = [0] * V
        path = []
        q = []
        q.append(starter_node)
        while len(q) > 0:
            x = q.pop(0)
            visited[x] = 1
            for i in range(V):
                for j in range(V):
                    if self.nodes[i][j] == 1 and visited[j] == 0:
                        q.append(j)
        for i in range(V):
            if visited[i] == 0:
                return False
        return True

if __name__ == '__main__':
    n = int(input())
    q = int(input())
    g = Graph(n)
    for i in range(q):
        line = input().split(' ')
        v = int(line[0])
        u = int(line[1])
        g.add_edge(v, u)
    mother = g.find_mother_vertex()
    print(mother)
